import numpy as np
import cv2

img = cv2.imread("messi.jpeg",0) #画像の読み込み
cv2.imshow('image',img) #画像をWindowで出す。画像の大きさに併せて自動でだす。
cv2.waitKey(0) & 0xFF #keyboard binding function
if k == 27:
    cv2.destroyAllWindows() #Windowをすべて消す。どれがでよければdestroyWindow()
elif k == ord('s'):
    cv2.imwrite('messigray.png', img) #Save an image
    cv2.destroyAllWindows()

