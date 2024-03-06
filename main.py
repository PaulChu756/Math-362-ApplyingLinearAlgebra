import cv2
import numpy as np

def rgb_to_hsv(rgb_image):
    """
    Convert an RGB image to HSV color space.

    Parameters:
    - rgb_image: Input RGB image (numpy array).

    Returns:
    - hsv_image: Output HSV image (numpy array).
    """
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    return hsv_image

def hsv_to_rgb(hsv_image):
    """
    Convert an HSV image to RGB color space.

    Parameters:
    - hsv_image: Input HSV image (numpy array).

    Returns:
    - rgb_image: Output RGB image (numpy array).
    """
    rgb_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)
    return rgb_image

def main():
    image_path = 'me.jpg'
    original_image = cv2.imread(image_path)

    # Ensure the image is in RGB format (OpenCV loads images in BGR by default)
    rgb_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

    # Perform RGB to HSV transformation
    hsv_result = rgb_to_hsv(rgb_image)

    # Perform HSV to RGB transformation
    rgb_result = hsv_to_rgb(hsv_result)

    # Display the original, RGB to HSV, and back to RGB images side by side
    cv2.imshow('Original Image', original_image)
    cv2.imshow('RGB to HSV', hsv_result)
    cv2.imshow('HSV to RGB', rgb_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
