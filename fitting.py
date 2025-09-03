import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

image_path = ''  # replace with your image path

BINARY_THRESHOLD = 120
CANNY_LOW = 30
CANNY_HIGH = 90


def load_and_preprocess_image(image_path, threshold_value):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError("Image file not found: " + image_path)
    ret, binary = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)
    return img, binary


def detect_black_points(binary_img):
    y_coords, x_coords = np.where(binary_img == 0)
    points = np.vstack((x_coords, y_coords)).T
    return points


def remove_duplicate_x(points):
    unique_x = np.unique(points[:, 0])
    merged_points = []
    for x in unique_x:
        ys = points[points[:, 0] == x][:, 1]
        y_avg = np.mean(ys)
        merged_points.append([x, y_avg])
    merged_points = np.array(merged_points)
    merged_points = merged_points[merged_points[:, 0].argsort()]
    return merged_points


def extract_edges(binary_img, canny_low, canny_high):
    edges = cv2.Canny(binary_img, canny_low, canny_high)
    return edges


def sine_model(x, A, B, C, D):
    return A * np.sin(B * x + C) + D


def fit_sine_curve(x_data, y_data):
    A_guess = (np.max(y_data) - np.min(y_data)) / 2
    D_guess = (np.max(y_data) + np.min(y_data)) / 2
    B_guess = 20
    C_guess = 0
    p0 = [A_guess, B_guess, C_guess, D_guess]
    try:
        params, cov = curve_fit(sine_model, x_data, y_data, p0=p0)
    except Exception as e:
        print("Sine curve fitting error:", e)
        params = None
    return params


def scale_data(merged_points):
    x = merged_points[:, 0]
    x_min, x_max = np.min(x), np.max(x)
    x_scaled = (x - x_min) / (x_max - x_min) * 0.3

    y = merged_points[:, 1]
    y_min, y_max = np.min(y), np.max(y)
    y_scaled = (y - y_min) / (y_max - y_min) * 1024 - 512

    return x_scaled, y_scaled


def main():
    img, binary = load_and_preprocess_image(image_path, BINARY_THRESHOLD)

    plt.title("Original Grayscale Image")
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.show()
    plt.title("Binarized Image (threshold={})".format(BINARY_THRESHOLD))
    plt.imshow(binary, cmap='gray')
    plt.axis('off')
    plt.show()

    black_points = detect_black_points(binary)
    print("Number of detected black points:", len(black_points))

    merged_points = remove_duplicate_x(black_points)

    plt.figure(figsize=(8, 8), dpi=300)
    plt.imshow(binary, cmap='gray')
    plt.scatter(merged_points[:, 0], merged_points[:, 1], c='red', s=10, label='Merged points')
    plt.title("Merged Black Points")
    plt.legend()
    plt.axis('off')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.show()

    edges = extract_edges(binary, CANNY_LOW, CANNY_HIGH)
    plt.figure(figsize=(8, 8), dpi=300)
    plt.imshow(edges, cmap='gray')
    plt.title("Edge Detection (Canny: low={}, high={})".format(CANNY_LOW, CANNY_HIGH))
    plt.axis('off')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.show()

    x_data, y_data = scale_data(merged_points)

    params = fit_sine_curve(x_data, y_data)
    if params is not None:
        A, B, C, D = params
        print("Fitted sine curve parameters:")
        print("A = {:.3f}, B = {:.3f}, C = {:.3f}, D = {:.3f}".format(A, B, C, D))
        fitted_sin_function = "f(t) = {:.3f} * sin({:.3f} * t + {:.3f}) + {:.3f}".format(A, B, C, D)
        print("Fitted sine function:", fitted_sin_function)
        print('Rotational speed:', B * 60 / (2 * np.pi), 'rpm')

        y_fit = sine_model(x_data, *params)
        plt.figure(figsize=(8, 4))
        plt.plot(x_data, y_fit, label='Fitted sine curve', color='red')
        plt.xlim(0, 0.3)
        plt.ylim(-512, 512)
        plt.xlabel("Time (s)")
        plt.ylabel("Frequency (Hz)")
        plt.title("Sine Curve Only")
        plt.legend()
        plt.show()
    else:
        print("Sine curve fitting failed!")


if __name__ == "__main__":
    main()
