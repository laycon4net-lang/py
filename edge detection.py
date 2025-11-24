import cv2, numpy as np, matplotlib.pyplot as plt

def display(title, img, cmap=cv2.COLOR_BGR2RGB):
    plt.imshow(cv2.cvtColor(img, cmap) if img.ndim==3 else img, cmap="gray")
    plt.title(title); plt.axis("off"); plt.show()

def edge_activity(path):
    img = cv2.imread(path); 
    if img is None: return print("❌ Not found")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    display("Original", img); display("Gray", gray)

    ops = {
        "1":("Sobel", lambda: cv2.bitwise_or(
            cv2.Sobel(gray,cv2.CV_64F,1,0,3).astype(np.uint8),
            cv2.Sobel(gray,cv2.CV_64F,0,1,3).astype(np.uint8))),
        "2":("Canny", lambda: cv2.Canny(
            gray, int(input("Lower (100):") or 100), int(input("Upper (200):") or 200))),
        "3":("Laplacian", lambda: cv2.Laplacian(gray,cv2.CV_64F).astype(np.uint8)),
        "4":("Gaussian Blur", lambda: cv2.GaussianBlur(
            img, (k:=(int(input("Kernel (5):") or 5),)*2)[0:2],0)),
        "5":("Median", lambda: cv2.medianBlur(img,int(input("Kernel (5):") or 5)))
    }

    while True:
        c=input("\n1.Sobel 2.Canny 3.Laplacian 4.Blur 5.Median 6.Exit: ")
        if c=="6": break
        if c in ops: t,f=ops[c]; display(t,f())
        else: print("⚠️ Invalid")

edge_activity("example.jpeg")
