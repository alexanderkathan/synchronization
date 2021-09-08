import matplotlib.pyplot as plt
import cv2
import time


def play_video_of_speaker():
    cap = cv2.VideoCapture("/home/kathanal/Sandbox/Demo_Synchronisation/Data/Train_DE_03.avi")
    _, frame = cap.read()

    while(True):
        _, frame = cap.read()
        cv2.imshow('Speaker A',frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    time.sleep(10)
    play_video_of_speaker()