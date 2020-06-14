import cv2
#Create a CascadeClassifier Object
face_cascade =cv2.CascadeClassifier("C:\\Users\\Engr Daniel Amoo\\Downloads\\haarcascade_frontalface_default.xml")

#Reading the image as it is
img=cv2.imread("C:\\Users\\Engr Daniel Amoo\\Pictures\\Screenshots\\Screenshot (107).png",1)

#Reading the image as gray scale image
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05, minNeighbors=15)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y), (x+w,y+h),(0,255,0),3)

cv2.imshow("Gray", img)

cv2.waitKey(0)
cv2.destroyAllWindows()