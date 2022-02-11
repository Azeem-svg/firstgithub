import cv2
import numpy as np
img = cv2.imread('bct.jpg', 0)
img1 = cv2.resize(img, (450,450))
seed_pt = (25, 25)
fill_color = 0
mask = np.zeros_like(img1)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
for th in range(60, 120):
    prev_mask = mask.copy()
    mask = cv2.threshold(img1, th, 255, cv2.THRESH_BINARY)[1]
    mask = cv2.floodFill(mask, None, seed_pt, fill_color)[1]
    mask = cv2.bitwise_or(mask, prev_mask)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

n_centers = cv2.connectedComponents(mask)[0] - 1
print('There are %d cells in the image.'%n_centers)
# import cv2
# import numpy as np

# img = cv2.imread('bct.jpg')
# img1 = cv2.resize(img, (450,450))
# mask = cv2.threshold(img1[:, :, 0], 255, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# stats = cv2.connectedComponentsWithStats(mask, 8)[2]
# label_area = stats[1:, cv2.CC_STAT_AREA]

# min_area, max_area = 50, 350  # min/max for a single circle
# singular_mask = (min_area < label_area) & (label_area <= max_area)
# circle_area = np.mean(label_area[singular_mask])

# n_circles = int(np.sum(np.round(label_area / circle_area)))

# print('Total circles:', n_circles)

cv2.imshow("Original", img1)
cv2.waitKey(0)

cv2.destroyAllWindows()