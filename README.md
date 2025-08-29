# Introduction
This project is based on the existing experimental platform, namely the AWR1642 millimeter-wave radar and DCA1000EVM data capture card of Texas Instruments.  
The objectives is as follows,
* Set up the experimental environment and obtain good radar echo data.
* Process the echo signal and extract its time-domain, frequency-domain and time-frequency characteristics.
* Based on the extracted image features, key characteristics of the unmanned aerial vehicle, including distance, azimuth angle, blade length, and rotation period are systematically identified and computed.
* The experimental data should be verified based on multiple methods.

Only **part of the project** — specifically my own work — are showcased in this repository.  
Entire codes and workflow will not be presented because it's a Collaborative Research and Development Project based on platform in our lab. 

The approaches applied in this project are **not yet fully developed**. This repository mainly serves as a record and summary.  

Discussions are welcome.

# Experimental Tools
We use the AWR1642BOOST mmWave Radar Sensor and DCA1000EVM Data-Capture Adapter.  
Please check the [Experimental_Tools](./Experimental_Tools) for more details.

# Experimental Setup
[Board to board connection](./Experimental_Setup/Board%20to%20board%20connection), [MMWAVE-STUDIO](./Experimental_Setup/MMWAVE-STUDIO), and [Interface of Sensor Configuration of MMWAVE-STUDIO](./Experimental_Setup/Interface%20of%20Sensor%20Configuration%20of%20MMWAVE-STUDIO) are presented in the filelist. You can do direct modification of configuration parameters based on your target.

# Related_defination
Please check [Related_defination](./Related_defination) if you do not familar with related definations like Doppler Effect and Micro-Doppler.

# Basic_Measurement_Theory
[Basic_Measurement_Theory](./Basic_Measurement_Theory) covers the rough idea to do the project-range measurement, angle measurement, STFT and Time-frequency distribution fitting. If you want to know more about the details or the inference process, please check the [Reference](#Reference).

# Outcomes
[Outcomes](./Outcomes) shows targets used in the experiment, radar imaging(RA heatmap, STFT heatmap), and the result of the feature extraction-the fitting curve(which can be obtained through the process of using Time–Frequency Distribution fitting algorithm-original grayscale image, binarized image, and scaled discrete data).  

We can obtain the distance and the azimuth angle from the RA heatmap.

We can compute the rotational speed and the blade length through the fitting curve

# Reference















