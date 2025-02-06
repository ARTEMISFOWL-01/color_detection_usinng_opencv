from PIL import Image
import numpy as np
import cv2
def limit_find(color):
    c=np.uint8([[color]])
    hsvc=cv2.cvtColor(c,cv2.COLOR_BGR2HSV)
    lowlim=hsvc[0][0][0]-10,100,100
    uplim=hsvc[0][0][0]+10,255,255
    lowlim=np.array(lowlim,dtype=np.uint8)
    uplim=np.array(uplim,dtype=np.uint8)
    return lowlim,uplim
yellow=[0,255,255]
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read();
    ll,ul=limit_find(yellow)
    hsvcimage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsvcimage,ll,ul)
    mask_=Image.fromarray(mask)
    bbox=mask_.getbbox()
    if bbox is not None:
        x1,y1,x2,y2=bbox
    frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)
    frame=cv2.putText(frame,text='yellow',org=(x1,y1),color=(0,0,255),fontFace=1,fontScale=1,thickness=2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break;
cap.release()
cv2.destroyAllWindows()
