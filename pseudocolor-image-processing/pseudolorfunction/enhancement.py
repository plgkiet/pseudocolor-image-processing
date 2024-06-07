import numpy as np
import matplotlib.pyplot as plt
import cv2

# Đọc ảnh grayscale
image_gray = cv2.imread('letter.png', cv2.IMREAD_GRAYSCALE)

# Chọn một dải màu phù hợp
cmap = plt.cm.jet



# Hiển thị dữ liệu bằng pseudocolor
plt.subplot(1, 2, 1)
plt.imshow(image_gray, cmap=cmap)
plt.colorbar()  # Thêm thanh màu cho biểu đồ
plt.title('Original Pseudocolor Plot')

# Tăng độ tương phản bằng histogram equalization
equ = cv2.equalizeHist(image_gray)

plt.subplot(1, 2, 2)
plt.imshow(equ, cmap=cmap)
plt.colorbar()
plt.title('Enhanced Pseudocolor Plot')

plt.show()
