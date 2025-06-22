import cv2
import numpy as np

class Seeker:

    def get_buton(self, model_image):
        hsv = cv2.cvtColor(model_image, cv2.COLOR_BGR2HSV)
        lower_violet = np.array([120, 50, 50])
        upper_violet = np.array([160, 255, 255])
        mask = cv2.inRange(hsv, lower_violet, upper_violet)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            return (cx, cy)
        return None