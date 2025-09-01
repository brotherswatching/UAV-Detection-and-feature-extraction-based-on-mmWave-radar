# Introduction
This project is based on the existing experimental platform, namely the AWR1642 millimeter-wave radar and DCA1000EVM data capture card of Texas Instruments.  
The objectives is as follows,
* Set up the experimental environment and obtain good radar echo data.
* Process the echo signal and extract its time-domain, frequency-domain and time-frequency characteristics.
* Based on the extracted image features, key characteristics of the unmanned aerial vehicle, including distance, azimuth angle, blade length, and rotation period are systematically identified and computed.
* The experimental data should be verified based on multiple methods.

Only **part of the project** — specifically what I've worked on — are showcased in this repository.  

The approaches applied in this project are **not yet fully developed**. This repository mainly serves as a record and a possible reference approach.  

Discussions are welcome.

# 1 Experimental Tools
We chose the AWR1642BOOST mmWave Radar Sensor together with the DCA1000EVM Data-Capture Adapter for this project. These two devices work in tandem to achieve the experimental objectives: transmitting and receiving radar echoes, capturing signals, and generating binary files. 

## 1.1 the AWR1642BOOST mmWave Radar Sensor

*the AWR1642BOOST mmWave Radar Sensor*
![the AWR1642BOOST mmWave Radar Sensor](./Experimental_Tools/AWR1642BOOST%20mmWave_Radar_Sensor.png)

Functional block diagram of AWR1642BOOST is a baisc thing you need to know in the project.
![Functional_block_diagram_of_AWR1642BOOST](./Experimental_Tools/Functional_block_diagram_of_AWR1642BOOST.png)

## 1.2 the DCA1000EVM Data-Capture Adapter

*the DCA1000EVM Data-Capture Adapter*
![the DCA1000EVM Data-Capture Adapter](./Experimental_Tools/Real-time_Data-Capture_Adapter_DCA1000EVM.png)

# 2 Experimental Setup
Essential preparation before the experiment.

## 2.1 Board to board connection
A simple instruction to connect the Experimental instruments.
![Board to board connection](./Experimental_Setup/Board_to_Board_Connection.png)

## 2.2 MMWAVE-STUDIO
MMWAVE-STUDIO is a software officially provided by Texas Instruments. It is a stand-alone Windows application that provides the ability to configure and control mmWave sensor modules and collect analog-to-digital (ADC) data for offline analysis.   
It provides a rich GUI interface, facilitating researchers to quickly debug it. And it supports multiple boards including DCA1000EVM and AWR1642BOOST.  

## 2.3 Interface of Sensor Configuration of MMWAVE-STUDIO

*Interface of Sensor Configuration of MMWAVE-STUDIO*
![Interface of Sensor Configuration of MMWAVE-STUDIO](./Experimental_Setup/Interface_of_Sensor_Configuration_of_MMWAVE-STUDIO.png)

You can do direct modification of configuration parameters based on your project objectives and target.

# 3 Related_defination
Two related definitions, namely the Doppler Effect and micro-Doppler.  
If you want to know more about the details or the inference process, please check the [Reference](#Reference).

## 3.1 Doppler Effect
The Doppler effect refers to the phenomenon that the frequency of the observed wave changes when there is relative motion between the source and the observer. This phenomenon applies to sound waves, light waves, electromagnetic waves and other types of fluctuations.


## 3.2 Micro-Doppler


# 4 Basic_Measurement_Theory
[Basic_Measurement_Theory](./Basic_Measurement_Theory) covers the rough idea to do the project-range measurement, angle measurement, STFT and Time-frequency distribution fitting.  
If you want to know more about the details or the inference process, please check the [Reference](#Reference). 
## 4.1 Range measurement

## 4.2 Angle measurement

## 4.3 STFT

## 4.4 Time-frequency distribution fitting

## 4.5 The model of the Rotating Target Echo

# 5 Outcomes
## 5.1 Targets used in the experiment

## 5.2 Radar imaging(RA heatmap)

## 5.3 Radar imaging(STFT heatmap)

## 5.4 the fitting curve

[Outcomes](./Outcomes) shows targets used in the experiment, radar imaging(RA heatmap, STFT heatmap), and the result of the feature extraction-the fitting curve(which can be obtained through the process of using Time–Frequency Distribution fitting algorithm-original grayscale image, binarized image, and scaled discrete data).  

We can obtain the distance and the azimuth angle from the RA heatmap.

We can compute the rotational speed and the blade length through the fitting curve

# Reference
[1] He, Binyu. "Research on UAV Target Micro-Doppler Spectrogram Recognition
Based on Deep Learning" [D]. University of Electronic Science and Technology of
China, 2023.  
[2] Gong, Ting. "Research on Radar Target Micro-Motion Parameter Estimation and
Micro-Motion Form Classification Technology" [D]. National University of Defense
Technology, 2020.  
[3] Qin X, Deng B, Wang H. Micro-Doppler Feature Extraction of Rotating
Structures of Aircraft Targets with Terahertz Radar[J]. Remote Sens, 2022, 14:3856.
https://doi.org/10.3390/rs14163856  
[4] Gao X, Xing G, Roy S, Liu H. Experiments with mmWave Automotive Radar
Test-bed[R]. University of Washington, [n.d.].Available from : https
//github.com/Xiangyu-Gao/mmWave-radar-signal-processing-and-microDopplerclassification  
[5] Ma J, Dong Y W, Li Y, et al. Multi-rotor UAV's micro-Doppler characteristic
analysis and feature extraction. Journal of University of Chinese Academy of
Sciences, 2019, 36(2): 235-243.  
[6] Chen, Yongbin, Li, Shaodong, Chen, Wenfeng, et al. "Modeling and
Characteristic Analysis of Helicopter Rotor Blade Echoes" [J]. Journal of the Air
Force Early Warning Academy, 2015, 29(05): 322-327.  
[7] Mmwave Radar Device ADC Raw Data Capture,Ti















