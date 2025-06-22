import pytesseract
import cv2
import numpy as np

class ScreenText:
    def __init__(self, driver):
        self.driver = driver

    def get_text_from_screen(self):
        screenshot = self.driver.get_screenshot_as_png()
        image = cv2.imdecode(np.frombuffer(screenshot, np.uint8), cv2.IMREAD_COLOR)
        text = pytesseract.image_to_string(image, lang='por')
        return text
