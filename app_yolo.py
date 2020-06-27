import cv2
import numpy as np
from scipy.spatial import distance
import sys

# Initialize the parameters
confThreshold = 0.5  #Confidence threshold
nmsThreshold = 0.4   #Non-maximum suppression threshold
inpWidth = 608      #Width of network's input image
inpHeight = 608      #Height of network's input image


# Model Net loading
net = cv2.dnn.readNetFromDarknet('yolov3.cfg','yolov3.weights')




bounding_box_color = np.random.uniform(0, 255, size=(40, 3))
videofile=sys.argv[1]
print(videofile)

camera=cv2.VideoCapture(videofile)

# Get the names of the output layers
def getOutputsNames(net):
# Get the names of all the layers in the network
    layersNames = net.getLayerNames()
# Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
while camera.isOpened():
    ret,img=camera.read()
    (h, w) = img.shape[:2]
    dist=[]
    index=[]
    ii=0
    confidences=[]
    boxes=[]
    img=cv2.resize(img,(608,608))
    blob = cv2.dnn.blobFromImage(img,0.00392, (608,608))
    net.setInput(blob)
    outs=net.forward(getOutputsNames(net))
    for out in outs:
        for detection in out:
            scores=detection[5:]
            class_id=np.argmax(scores)
            if class_id==0:

                cx=int(detection[0]*608)
                cy=int(detection[1]*608)
                wid=int(detection[2]*608)
                heig=int(detection[3]*608)
                confidence=scores[0]
                left=cx-int(wid/2)
                top=cy-int(heig/2)
                boxes.append([left,top,wid,heig])
                confidences.append(float(confidence))
                
    indexes=cv2.dnn.NMSBoxes(boxes,confidences,0.5,0.4)
    for i in indexes:
        i=i[0]
        box=boxes[i]
        startX=box[0]
        startY=box[1]
        endX=startX+box[2]
        endY=box[3]+startY
        midx=int((startX+endX)/2)
        midy=int((startY+endY)/2)
        dist.append([startX,startY,endX,endY,midx,midy])
        cv2.circle(img,(midx,midy),1,(0,255,255),2)
    alert=[False for i in range(len(dist))]
    
    for j in range(len(dist)):
        for k in range(j+1,len(dist)):
            if alert[j]==True:
                break
            eucli=distance.euclidean((dist[j][4],dist[j][5]),(dist[k][-2],dist[k][-1]))
            
            if(eucli<150):
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


    

