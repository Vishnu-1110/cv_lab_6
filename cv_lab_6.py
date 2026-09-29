import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image in grayscale
img = cv2.imread("image2.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found")
else:
    plt.figure(figsize=(12, 10))

    # Original image
    plt.subplot(3, 3, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Original Image")
    plt.axis("off")

    # Display all 8 bit planes
    for i in range(8):
        bit_plane = (img >> i) & 1
        vis_plane = bit_plane * 255

        plt.subplot(3, 3, i + 2)
        plt.imshow(vis_plane, cmap="gray")
        plt.title(f"Bit Plane {i}")
        plt.axis("off")

    plt.tight_layout()
    plt.show()
