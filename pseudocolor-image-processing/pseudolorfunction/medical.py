import numpy as np
import matplotlib.pyplot as plt
import cv2


# Đọc ảnh grayscale
image_gray = cv2.imread('medical.png', cv2.IMREAD_GRAYSCALE)

# Chọn một dải màu phù hợp
cmap = plt.cm.jet

# Hiển thị dữ liệu bằng pseudocolor
plt.imshow(image_gray, cmap=cmap)
plt.colorbar()  # Thêm thanh màu cho biểu đồ
plt.title('Pseudocolor Plot')

plt.show()
