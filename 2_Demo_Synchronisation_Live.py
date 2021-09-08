#!/usr/bin/env python
# coding: utf-8

import opensmile
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.filters import gaussian_filter1d
import os


# Extract ComParE_2016 Features for both Speakers with OpenSmile
def extract_features():
    smile = opensmile.Smile(
        feature_set=opensmile.FeatureSet.ComParE_2016,
        feature_level=opensmile.FeatureLevel.LowLevelDescriptors,
    )

    speaker_a = smile.process_file('./Data/Train_DE_03_trimmed_long.wav')
    speaker_b = smile.process_file('./Data/Train_DE_23_trimmed_long.wav')

    return speaker_a,speaker_b


# Calculate the mean-value of a specific feature within a specific time window for a speaker
def calculate_mean_feature(speaker,feature,time_window):
    ctr = 0
    current_sum = 0
    current_mean = 0
    mean_feature_interval = []
    stop = time_window

    for i in range(len(speaker)):
        if i%stop == 0: 
            _discard = False
            interval = speaker.iloc[i:i+stop][feature]
            for value in interval:
                if value < 0.05:
                    _discard = True
                    break
            
            if _discard:
                mean_feature_interval.append(current_mean)
                continue
            
            current_mean = np.mean(interval)

            mean_feature_interval.append(current_mean)
    
    return mean_feature_interval
 

# Smooth and plot data
def visualize_live_curve(diff,speaker_a,speaker_b):
    smoothed_diff = gaussian_filter1d(diff, sigma=50)
    smoothed_speaker_a = gaussian_filter1d(speaker_a, sigma=50)
    smoothed_speaker_b = gaussian_filter1d(speaker_b, sigma=50)

    fig, axis = plt.subplots(1,2,figsize=(15,5))

    x_axis = np.arange(0, 165, 0.15)

    axis[1].axis([0, 1120, -170, 170])
    axis[0].axis([0, 1120, 0, 620])
    
    plt.setp(axis[1],xlabel="Time [s]")
    plt.setp(axis[1],ylabel="Mean Pitch Difference")
    plt.setp(axis[0],xlabel="Time [s]")
    plt.setp(axis[0],ylabel="Mean Pitch")

    axis[0].set_xticks(np.arange(0, 170, 20))
    axis[0].set_yticks(np.arange(0, 620, 100))
    axis[0].set_yticks(np.arange(0, 620, 50), minor=True)

    axis[1].set_xticks(np.arange(0, 170, 20))
    axis[1].set_xticks(np.arange(0, 170, 20), minor=True)
    axis[1].set_yticks(np.arange(-200, 200, 50))
    axis[1].set_yticks(np.arange(-200, 200, 50), minor=True)


    for i in range(len(diff)):
        axis[0].clear()
        axis[1].clear()
        plt.setp(axis[1],xlabel="Time [s]")
        plt.setp(axis[1],ylabel="Mean Pitch Difference")
        plt.setp(axis[0],xlabel="Time [s]")
        plt.setp(axis[0],ylabel="Mean Pitch")
        axis[1].axis([0, 170, -200, 200])
        axis[0].axis([0, 170, 0, 620])
        axis[1].plot(x_axis[:i],smoothed_diff[:i],color="green")
        axis[0].plot(x_axis[:i],smoothed_speaker_a[:i],color="blue",label="Speaker A")
        axis[0].plot(x_axis[:i],smoothed_speaker_b[:i],color="red",label="Speaker B")


        axis[0].legend(loc="best")
        

        axis[0].grid(which='both')
        axis[1].grid(which='both')

        axis[0].grid(which='minor', alpha=0.2)
        axis[0].grid(which='major', alpha=0.5)
        axis[1].grid(which='minor', alpha=0.2)
        axis[1].grid(which='major', alpha=0.5)

        plt.pause(0.1)

    plt.show()


if __name__ == "__main__":
    speaker_a,speaker_b = extract_features()

    mean_pitch_a = calculate_mean_feature(speaker=speaker_a,feature='F0final_sma',time_window=15)
    mean_pitch_b = calculate_mean_feature(speaker=speaker_b,feature='F0final_sma',time_window=15)

    mean_pitch_diff = np.array(mean_pitch_a) - np.array(mean_pitch_b)

    visualize_live_curve(mean_pitch_diff,mean_pitch_a,mean_pitch_b)