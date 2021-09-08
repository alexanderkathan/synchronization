import matplotlib.pyplot as plt
import cv2
import time


def play_video_of_speaker():
    cap = cv2.VideoCapture("/home/kathanal/Sandbox/Demo_Synchronisation/Data/spectrogram_bottom_trimmed.mp4")
    _, frame = cap.read()

    while(True):
        _, frame = cap.read()
        cv2.imshow('Spectrogram',frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    time.sleep(10)
    play_video_of_speaker()
