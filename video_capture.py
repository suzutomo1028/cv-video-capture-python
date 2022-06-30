#!/usr/bin/env python3

import cv2

def video_capture():
    cap_cam = cv2.VideoCapture(0)
    if cap_cam.isOpened():
        while True:
            ret, frame = cap_cam.read()
            if ret is True:
                cv2.imshow('Capture', frame)
                key = cv2.waitKey(1)
                if key == ord('s'):
                    cv2.imwrite('capture.jpg', frame)
                elif key == ord('q'):
                    cv2.destroyAllWindows()
                    break
    cap_cam.release()

if __name__ == '__main__':
    video_capture()
