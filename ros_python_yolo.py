#在ros中使用torch.hub.load加载yolo检测模型
import rospy
import cv2
import yolov5
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import torch

class test():
    def __init__(self):
        self.bridge = CvBridge()
        self.detect = torch.hub.load('ultralytics/yolov5', 'yolov5s') #从网络中加载yolo模型
        
        
    def subcriber(self):
        #img = rospy.wait_for_message('/usb_cam/image_raw', Image)
        img = rospy.wait_for_message('/usb_cam/image_raw', Image)
        print('work1')
        return img
    
    def image_detect(self, img):
        bridge = CvBridge()
        img = bridge.imgmsg_to_cv2(img, "bgr8")
        #img = cv2.cvtColor(imgC, cv2.COLOR_RGB2GRAY)
        print(img.shape)
        
        result = self.detect(img)
        #print(result)
        result.print()
        
def main():
    rospy.init_node('test', anonymous=True)
    test_ = test()
    #print('work')
    while(1):
        img = test_.subcriber()
        #print('work2')
        test_.image_detect(img)
    
if __name__=='__main__':
    main()
    