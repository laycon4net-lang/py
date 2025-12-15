import cv2, numpy as np
def apply_filter(img, f):
    g =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if f in ['r','g','b']:
        c = {'r':(1,2), 'g':(0,2), 'b':(0,1)}[f]
        img[:,:,c[0]] = img[:,:,c[1]] = 0
    elif f== 's':
        s =cv2.Sobel(g, cv2.CV_64F, 1, 0, 3) + cv2.Sobel(g, cv2.CV_64F, 0, 1, 3)
        img = cv2.cvtColor(np.uint8(np.abs(s)),  cv2.COLOR_GRAY2BGR)
    elif f == 'c':
        img = cv2.cvtColor(cv2.Canny(g, 100, 200), cv2.COLOR_GRAY2BGR)
    return img
img = cv2.imread('example.jpeg')
if img is None: exit("Image not found!")
print("keys: r-red, g-green, b-blue, s-sobel, c-canny, q-quit")
f = '0' 
while True:
    cv2.imshow("Filter", apply_filter(img.copy(), f))
    k = cv2.waitKey(0) & 0xFF
    if k in map(ord, 'rgbsc'): f = chr(k)
    elif k == ord('q'): break
cv2.destroyAllWindows()