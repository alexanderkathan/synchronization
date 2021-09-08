# Demo Synchronization
In this project we show how audio features can be used to determine the synchronisation of people in conversations.

## Data
The relevant data (in order to be able to run these scripts) can be found in the NAS of the UAU under: \data_work\Alex\arte\Demonstrator

## How to use
* 1_start_demo.sh: This file starts all the following files (2-5) simultaniously (Important: Before you run it, make sure to edit the correct data file paths (due to data licences, the data can not be provided in this GitHub repo)
* 2_Demo_Synchronisation_Live.py: This file extracts the audio features and plot them for the different speakers.
* 3_Demo_Synchronisation_Play_Video_Speaker_A.py: This file plays the video of speaker A.
* 4_Demo_Synchronisation_Play_Video_Speaker_B.py: This file plays the video of speaker B.
* 5_Demo_Synchronisation_Play_Video_Spectrogram.py: This file plays a video of an extracted spectrogram of the original audio file.
* Demo_Synchronisation_Live.ipynb: Jupyter notebook for different tests