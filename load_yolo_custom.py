import torch 
import cv2
import time


cap = cv2.VideoCapture(0)

'''
设置YOLO模型参数，从本地加载YOLO模型
'''
detect = torch.hub.load('/home/zac/zac/yolov5/', 'custom', path='/home/zac/zac/Mproject/data/model/yolov5s.pt', source='local')



#start 
while(True):
    start_time = time.time() 
    ret, img = cap.read()
    a = 1
    #print(img)
    #cv2.imshow('noob', img)
    #cv2.waitKey(1)
    cv_time = time.time()
    result = detect(img)
    result.show()
    prediction = result.pandas().xyxy[0]
    print(result.pandas().xyxy)
    #cv2.rectangle(img, (result.pandas().xyxy[0]['xmin'], result.pandas().xyxy[0]['ymin']), (result.pandas().xyxy[0]['xmax'], result.pandas().xyxy[0]['ymax']), (255, 0, 255), 5)
    cv2.imshow('img', img)
    cv2.waitKey(1)
    end_time = time.time()
    cv_show_times = cv_time - start_time
    yolo_times = end_time - cv_time
    #print('cv_time', cv_show_times, 'yolo_time', yolo_times)
    #print(prediction['class'].values.tolist())