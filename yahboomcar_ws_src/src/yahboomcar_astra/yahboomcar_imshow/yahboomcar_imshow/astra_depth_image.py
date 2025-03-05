import rclpy
from rclpy.node import Node
import cv2 as cv
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class AstraDepthImage(Node):
    def __init__(self,name):
        super().__init__(name)
        self.bridge = CvBridge()
        self.sub_img = self.create_subscription(Image,'/camera/depth/image_raw',self.handleTopic,1)
        self.pub_img = self.create_publisher(Image,'/cv_image/depth',10)

    def handleTopic(self,msg):
        if not isinstance(msg, Image): return
        frame = self.bridge.imgmsg_to_cv2(msg, "16UC1")
        # 规范输入图像大小
        # Standardize the input image size
        frame = cv.resize(frame, (640, 480))
        cv.putText(frame, "cv_depth", (280, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (65536, 65536, 65536), 2)
        # opencv mat ->  ros msg
        msg = self.bridge.cv2_to_imgmsg(frame, "16UC1")
        self.pub_img.publish(msg)

def main():
    rclpy.init()
    get_astra_depth = AstraDepthImage('get_astra_depth_node')
    rclpy.spin(get_astra_depth)
