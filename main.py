import cv2
import numpy as np

MAX_HUE = 180

def rgb_to_hsv(rgb_image):
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    return hsv_image

def hsv_to_rgb(hsv_image):
    rgb_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)
    return rgb_image

def apply_random_hue(hsv_image):
    hsv_with_random_hue = hsv_image.copy()
    hsv_with_random_hue[:, :, 0] = np.random.randint(0, MAX_HUE, hsv_image.shape[:2])
    return hsv_with_random_hue

def apply_random_hue_per_row(hsv_image):
    hsv_with_random_hue = hsv_image.copy()

    for row in range(hsv_image.shape[0]):
        random_hue = np.random.randint(0, 180)
        hsv_with_random_hue[row, :, 0] = random_hue

    return hsv_with_random_hue

def apply_crazy_effect(hsv_image):
    hsv_psychedelic = hsv_image.copy()

    for col in range(hsv_image.shape[1]):
        hue_shift = col / hsv_image.shape[1] * MAX_HUE
        hsv_psychedelic[:, col, 0] = (hsv_image[:, col, 0] + hue_shift) % MAX_HUE

    return hsv_psychedelic



def main():
    image_path = 'me.jpg'
    original_image = cv2.imread(image_path)

    # Ensure the image is in RGB format (OpenCV loads images in BGR by default)
    rgb_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

    # Perform RGB to HSV transformation
    hsv_result = rgb_to_hsv(rgb_image)

    # Apply a psychedelic effect to the HSV image, smoothly transitioning hue values across columns
    hsv_result_crazy_effect = apply_crazy_effect(hsv_result)

    # Perform HSV to RGB transformation using the HSV image with random hue
    rgb_result = hsv_to_rgb(hsv_result_crazy_effect)

    # Display the original, RGB to HSV, RGB to HSV with random hue, and HSV to RGB images side by side
    cv2.imshow('0. Original Image', original_image)
    cv2.imshow('1. RGB', rgb_image)
    cv2.imshow('2. RGB to HSV', hsv_result)
    cv2.imshow('3. Psychedelic effect', hsv_result_crazy_effect)
    cv2.imshow('4. HSV to RGB', rgb_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
