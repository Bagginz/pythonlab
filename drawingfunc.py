import cv2
img = cv2.imread('images/bew.jpg')
img = cv2.putText(img, "Bew",(10,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
