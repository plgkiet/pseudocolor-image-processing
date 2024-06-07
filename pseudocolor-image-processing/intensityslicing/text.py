import cv2
import numpy as np

filename = 'X-ray.png'

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
original_img = img.copy()

r, c = img.shape
R = np.zeros((r, c), dtype=np.uint8)
G = np.zeros((r, c), dtype=np.uint8)
B = np.zeros((r, c), dtype=np.uint8)

# Số lượng slice mong muốn
nos = 2

# Chỉnh thông số theo ý muốn
# Tùy chỉnh khoảng độ sáng
interval = np.array([
    [0, 200],
    [200, 255],
]
)

# Tùy chỉnh màu sắc
color = np.array([
    [255, 0, 0],     
    [0, 0, 0], 
]
) 

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
