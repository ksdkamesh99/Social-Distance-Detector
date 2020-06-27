import cv2
import numpy as np
from scipy.spatial import distance
import sys
# Model Net loading

net = cv2.dnn.readNetFromCaffe('deploy.prototxt','mobilenet_iter_73000.caffemodel')


# Classes

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
     "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
     "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
     "sofa", "train", "tvmonitor"]

videofile=sys.argv[1]
print(videofile)
bounding_box_color = np.random.uniform(0, 255, size=(40, 3))
camera=cv2.VideoCapture(videofile)
while camera.isOpened():
    ret,img=camera.read()
    (h, w) = img.shape[:2]
    dist=[]
    index=[]
    ii=0
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections=net.forward()
    conf=[]
    boxes=[]
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        class_id = int(detections[0, 0, i, 1])
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype('int')
        midx=int((startX+endX)/2)
        midy=int((startY+endY)/2)


            # Filtering only persons detected in the frame. Class Id of 'person' is 15
        if class_id == 15.00:
            if(confidence>0.5):
                dist.append([startX,startY,endX,endY,midx,midy])
                index.append(ii)
                ii=ii+1
        
                # Draw bounding box for the object
                cv2.circle(img,(midx,midy),1,(0,255,255),2)
    alert=[False for i in range(len(dist))]
    
    for j in range(len(dist)):
        for k in range(j+1,len(dist)):
            if alert[j]==True:
                break
            eucli=distance.euclidean((dist[j][4],dist[j][5]),(dist[k][-2],dist[k][-1]))
            
            if(eucli<200):
                alert[j]=True
                alert[k]=True
    for k in range(len(alert)):
        startX=dist[k][0]
        startY=dist[k][1]
        endX=dist[k][2]
        endY=dist[k][3]
        if(alert[k]==True):
            cv2.rectangle(img, (startX, startY), (endX, endY),(0,0,255), 2)
        else:
            cv2.rectangle(img, (startX, startY), (endX, endY), (0,255,0), 2)
    saf=alert.count(False)
    cv2.putText(img,"Total Persons Detected : "+str(len(alert)),(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    cv2.putText(img,"No of Safe Persons Detected : "+str(saf),(50,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2)
    cv2.putText(img,"No of Unsafe Persons Detected : "+str(len(alert)-saf),(50,150),cv2.FONT_HERSHEY_SIMPLEX,1,(25,24,25),2)


    cv2.imshow("win",img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        camera.release()
        cv2.destroyAllWindows()


    

