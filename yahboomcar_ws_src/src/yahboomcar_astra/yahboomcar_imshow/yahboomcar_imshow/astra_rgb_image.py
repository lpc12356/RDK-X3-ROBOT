import rclpy
from rclpy.node import Node
import cv2 as cv
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class AstraRGBImage(Node):
    def __init__(self,name):
        super().__init__(name)
        self.bridge = CvBridge()
        self.sub_img = self.create_subscription(Image,'/camera/color/image_raw',self.handleTopic,1)
        self.pub_img = self.create_publisher(Image,'/cv_image/rgb',10)

    def handleTopic(self,msg):
        if not isinstance(msg, Image): return
        frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        # 规范输入图像大小
        # Standardize the input image size
        frame = cv.resize(frame, (640, 480))
        cv.putText(frame, "cv_rgb", (280, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        # opencv mat ->  ros msg
        msg = self.bridge.cv2_to_imgmsg(frame, "bgr8")
        self.pub_img.publish(msg)

def main():
    rclpy.init()
    get_astra_rgb = AstraRGBImage('get_astra_rgb_node')
    rclpy.spin(get_astra_rgb)
