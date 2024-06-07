import cv2
import numpy as np

# Đọc ảnh
filename = 'brain.png'

img = cv2.imread(filename)
original_img = img.copy()

# Phân đoạn hình ảnh (Ví dụ: Sử dụng phân đoạn dựa trên ngưỡng)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Tìm contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Tính toán giá trị trung bình của phần vùng quan tâm
mean_color = cv2.mean(img, mask=thresh)

# Xác định khoảng màu nổi bật
# Ví dụ: Sử dụng khoảng màu từ giá trị trung bình +/- một ngưỡng
threshold = 50
lower_color = np.array([max(0, mean_color[i] - threshold) for i in range(3)], dtype=np.uint8)
upper_color = np.array([min(255, mean_color[i] + threshold) for i in range(3)], dtype=np.uint8)

# Tạo màu pseudo
pseudo_color = np.random.randint(0, 255, (1, 3), dtype=np.uint8)

# Gán màu pseudo cho phần vùng quan tâm
mask = cv2.inRange(img, lower_color, upper_color)
img[mask != 0] = pseudo_color

# Hiển thị ảnh
cv2.imshow('Original Image', original_img )
cv2.imshow('Pseudo Color Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
