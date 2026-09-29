# Computer Vision Lab 6 — Bit Plane Slicing

This project demonstrates **bit plane slicing** of a grayscale image using Python, OpenCV, NumPy, and Matplotlib.

## Objective

To extract and visualize all **8 bit planes (0 to 7)** of a grayscale image and observe the information represented at each bit level.

## Libraries Used

- Python
- OpenCV
- NumPy
- Matplotlib

## Python Code

The complete program is available in [cv_lab_6.py](cv_lab_6.py).

## How It Works

A grayscale image contains pixel values from 0 to 255, which can be represented using 8 binary bits.

The program:

1. Reads the image in grayscale.
2. Extracts each bit plane from **Bit Plane 0** to **Bit Plane 7**.
3. Converts each binary plane to a visible black-and-white image.
4. Displays the original image along with all 8 bit planes.

### Bit Plane Slicing

The following operation extracts the i-th bit:

```python
bit_plane = (img >> i) & 1
```

The extracted plane is multiplied by 255 so that the 0 and 1 values can be displayed clearly as black and white.

## How to Run

Install the required libraries:

```bash
pip install opencv-python numpy matplotlib
```

Place the input image in the project folder with the name:

```text
image2.jpg
```

Run the program:

```bash
python cv_lab_6.py
```

This version uses a normal local image path. **No Google Colab or Google Drive connection is required.**

## Output

The program displays the original image and all 8 bit planes.

### Output Image

<img width="1189" height="878" alt="image" src="https://github.com/user-attachments/assets/9175b32c-6be1-4720-a951-59e5f56f0f64" />


## Result

The output shows how image information is distributed across the eight bit planes. Lower-order planes contain finer intensity variations, while higher-order planes reveal more prominent image structures.

## Author

**Vishnu Vardhan**

GitHub: [Vishnu-1110](https://github.com/Vishnu-1110)
