import cv2
import numpy

image = cv2.imread('solarsys.jpg')
cv2.putText(image,"sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(image,"mercury",(250,320),cv2.FONT_HERSHEY_COMPLEX,0.5,(100,100,255))
cv2.putText(image,"venus",(335,295),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,100,100))
cv2.putText(image,"earth",(435,295),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
cv2.putText(image,"mars",(535,295),cv2.FONT_HERSHEY_COMPLEX,0.5,(100,100,255))
cv2.putText(image,"jupiter",(685,320),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,255))
cv2.putText(image,"saturn",(900,295),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,100,100))
cv2.putText(image,"uranus",(1200,295),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
cv2.putText(image,"neptune",(1350,295),cv2.FONT_HERSHEY_COMPLEX,0.5,(100,200,255))
cv2.putText(image,"pluto",(1425,295),cv2.FONT_HERSHEY_COMPLEX,0.5,(100,200,255))
cv2.imshow("image",image)

cv2.imwrite("solarsys.jpg", image)

cv2.waitKey(0)
