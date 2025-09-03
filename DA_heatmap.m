clear;
close all;

[jsonFileId,errMsg] = fopen('','r');
rawJsonText = fscanf(jsonFileId,'%s');
fclose(jsonFileId);
mmwParams = jsondecode(rawJsonText);%%解析json文本
%%
adcFmt = mmwParams.mmWaveDevices.rfConfig.rlAdcOutCfg_t.fmt.b2AdcOutFmt;
rfProfileCfg = mmwParams.mmWaveDevices.rfConfig.rlProfiles.rlProfileCfg_t;
%%chirp配置
nSample = rfProfileCfg.numAdcSamples;
frameCfg = mmwParams.mmWaveDevices.rfConfig.rlFrameCfg_t;
%%帧配置
mimoflag = frameCfg.chirpEndIdx-frameCfg.chirpStartIdx;
nLoops = frameCfg.numLoops; %每帧chirps
file_id = fopen('','rb');

data = fread(file_id,Inf,'int16');
fclose(file_id);
nFrame = frameCfg.numFrames;
if mimoflag
    nRx = 8;
else 
    nRx = 4;
end
dataMat = zeros(nSample,nLoops,nRx,nFrame);%%采样数*脉冲数*接收天线数*帧数
for ii = 1:nFrame
    for jj = 1:nLoops
        for kk = 1:nRx
            start = (ii-1)*nRx*nLoops*nSample*2+(jj-1)*nRx*nSample*2+(kk-1)*nSample*2;
            rxData = data((start + 1):(start + 2*nSample));
            dataMat(1:2:end,jj,kk,ii) = rxData(1:4:end)+rxData(3:4:end)*1j;
            dataMat(2:2:end,jj,kk,ii) = rxData(2:4:end)+rxData(4:4:end)*1j;
        end
    end
end

%%计算带宽与距离单元
BW = mmwParams.mmWaveDevices.rfConfig.rlProfiles.rlProfileCfg_t.numAdcSamples/(mmwParams.mmWaveDevices.rfConfig.rlProfiles.rlProfileCfg_t.digOutSampleRate*1e3)...
    *(mmwParams.mmWaveDevices.rfConfig.rlProfiles.rlProfileCfg_t.freqSlopeConst_MHz_usec*1e12);
rangeBinWidth = 1/BW*3e8/2;

%多普勒分辨单元宽度
PRT = (mmwParams.mmWaveDevices.rfConfig.rlProfiles.rlProfileCfg_t.idleTimeConst_usec+mmwParams.mmWaveDevices.rfConfig.rlProfiles.rlProfileCfg_t.rampEndTime_usec)*1e-6;
c=3e8;
fc=77e9;
lambda = c/fc;
vMax = lambda/2/PRT;

y = ((1:nSample)-1)*rangeBinWidth;
x = ((1:nLoops)-1)*(vMax/nLoops);
[x,y] = meshgrid(x,y);
RDdata = squeeze(dataMat( : , : , 1, 1));%快时间采样*脉冲数
figure(1);mesh(x,y,abs(fft2(RDdata)));
xlabel('速度 m/s');ylabel('距离 m');

nFFT = 512;
rangeBinWidthZeroPad = rangeBinWidth/(nFFT/nSample);
y = ((1 : nFFT)-1)*rangeBinWidthZeroPad;
x = asind((1 : nFFT)/nFFT*2-1);
[x,y] = meshgrid(x,y);
RAdata = squeeze(dataMat( : , 1 , : , 1));%快时间*天线数
figure(2);mesh(x,y,fftshift(abs(fft2(RAdata,nFFT,nFFT)),2));
xlabel('角度 度');ylabel('距离 m');


