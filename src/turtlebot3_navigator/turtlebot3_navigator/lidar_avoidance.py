
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoider(Node):
    def __init__(self):
        super().__init__('obstacle_avoider')
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.laser_sub = self.create_subscription(LaserScan, '/scan', self.laser_callback, 10)

    def laser_callback(self, msg):
        twist = Twist()

        front = min(min(msg.ranges[0:10] + msg.ranges[-10:]), 10.0)
        left = min(msg.ranges[80:100])  # adjust based on angle resolution
        right = min(msg.ranges[260:280])  # same
#DP
        if front < 0.5:
            twist.linear.x = 0.0
            twist.angular.z = -0.5  # turn right
        elif left > 0.6:
            twist.linear.x = 0.0
            twist.angular.z = 0.5   # turn left to find wall
        else:
            twist.linear.x = 0.15
            twist.angular.z = 0.0   # follow wall

        self.cmd_vel_pub.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
