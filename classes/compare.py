import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

class Compare:

    def __init__(self):
        self.output_dir = os.path.join(os.path.dirname(__file__), '../images')

    def open_images(self):
        figma_path = os.path.join(os.path.dirname(__file__), '../images/golden_sample.png')
        built_path = os.path.join(os.path.dirname(__file__), '../images/screenshot.png')  # Corrigido aqui
        figma_img = cv2.imread(os.path.abspath(figma_path))
        built_img = cv2.imread(os.path.abspath(built_path))
        return figma_img, built_img, built_path

    def compare_images(self):
        figma_img, built_img, built_path = self.open_images()

        # Ensure images are the same size
        figma_img = cv2.resize(figma_img, (built_img.shape[1], built_img.shape[0]))

        # Convert images to grayscale
        figma_gray = cv2.cvtColor(figma_img, cv2.COLOR_BGR2GRAY)
        built_gray = cv2.cvtColor(built_img, cv2.COLOR_BGR2GRAY)

        # Compute SSIM between the two images
        (score, diff) = ssim(figma_gray, built_gray, full=True)

        # The diff image contains the actual image differences
        diff = (diff * 255).astype("uint8")

        # Threshold the difference image, followed by finding contours
        thresh = cv2.threshold(
            diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        contours = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]

        # Create a mask image that we will use to visualize the differences
        mask = np.zeros(figma_img.shape, dtype='uint8')
        filled_after = figma_img.copy()

        for c in contours:
            area = cv2.contourArea(c)
            if area > 40:
                x, y, w, h = cv2.boundingRect(c)
                figma_img = cv2.rectangle(
                    figma_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                built_img = cv2.rectangle(
                    built_img, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # Compare the region in both images
                figma_region = figma_gray[y:y+h, x:x+w]
                built_region = built_gray[y:y+h, x:x+w]

                if np.mean(figma_region) > np.mean(built_region):
                    # More white in Figma, use green
                    cv2.drawContours(filled_after, [c], 0, (0, 255, 0), -1)
                else:
                    # More white in built, use red
                    cv2.drawContours(filled_after, [c], 0, (0, 0, 255), -1)

        # Create the comparison image
        comparison = np.hstack((figma_img, built_img))

        # Update the comparison image path
        comparison_filename = f'comparison_{datetime.now().strftime("%Y%m%d_%H%M%S")}.jpg'
        comparison_path = os.path.join(self.output_dir, comparison_filename)
        cv2.imwrite(comparison_path, comparison)
