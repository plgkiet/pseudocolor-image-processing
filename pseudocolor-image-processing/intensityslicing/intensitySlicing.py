import cv2
import numpy as np

filename = 'color.png'

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
original_img = img.copy()

r, c = img.shape
R = np.zeros((r, c), dtype=np.uint8)
G = np.zeros((r, c), dtype=np.uint8)
B = np.zeros((r, c), dtype=np.uint8)

# Số lượng slice mong muốn
nos = 10

# Chỉnh thông số theo ý muốn
# Tùy chỉnh khoảng độ sáng
interval = np.array([
    [0, 25],
    [26, 51],
    [52, 77],
    [78, 102],
    [103, 128],
    [129, 154],
    [155, 179],
    [180, 205],
    [206, 230],
    [231, 255]
]
)

# Tùy chỉnh màu sắc
color = np.array([
    (255, 0, 0),     # Đỏ
    (0, 255, 0),     # Xanh lá cây
    (0, 0, 255),     # Xanh dương
    (255, 255, 0),   # Vàng
    (255, 0, 255),   # Tím
    (0, 255, 255),   # Cyan
    (128, 0, 0),     # Đỏ tối
    (0, 128, 0),     # Xanh lá cây tối
    (0, 0, 128),     # Xanh dương tối
    (128, 128, 128)  # Xám
]
) 

# # Random màu và độ sáng
# color = np.zeros((nos, 3), dtype=np.uint8)
# interval = np.zeros((nos, 2))
# for i in range(nos):
#     interval[i, :] = [0,255]
#     color[i, :] = np.uint8(255 * np.random.rand(3))


# Gán pseudo-màu dựa trên các giá trị độ sáng của ảnh mức xám
for s in range(nos):
    LL, UL = map(int, interval[s, :])
    red, green, blue = color[s, :]

    for i in range(r):
        for j in range(c):
            if LL <= img[i, j] <= UL:
                R[i, j] = red
                G[i, j] = green
                B[i, j] = blue

# Hợp nhất kênh màu
imgc = cv2.merge((R, G, B))

# HIển thị hình ảnh
cv2.imshow('Original image', original_img)
cv2.imshow('Pseudo Color Image', imgc)
cv2.waitKey(0)
cv2.destroyAllWindows()
