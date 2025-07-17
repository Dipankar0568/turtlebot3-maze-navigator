#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, NavigationResult
import time

class MazeNavigator(Node):
    def __init__(self):
        super().__init__('maze_navigator')
        self.navigator = BasicNavigator()

        # Wait for Nav2 to be active
        self.navigator.wait_until_nav2_active()

        # Define waypoints as a list of PoseStamped
        waypoints = [
            self.create_pose(1.0, 0.0, 0.0),
            self.create_pose(2.0, 0.0, 0.0),
            self.create_pose(2.0, 1.0, 0.0),
            self.create_pose(1.0, 1.0, 0.0)
        ]

        # Send goals sequentially
        for pose in waypoints:
            self.navigator.go_to_pose(pose)
            while not self.navigator.is_task_complete():
                time.sleep(0.5)
            result = self.navigator.get_result()
            if result == NavigationResult.SUCCEEDED:
                self.get_logger().info('Goal succeeded!')
            else:
                self.get_logger().warn('Goal failed!')

        rclpy.shutdown()

    def create_pose(self, x, y, yaw):
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.position.z = 0.0
        from tf_transformations import quaternion_from_euler
        q = quaternion_from_euler(0, 0, yaw)
        pose.pose.orientation.x = q[0]
        pose.pose.orientation.y = q[1]
        pose.pose.orientation.z = q[2]
        pose.pose.orientation.w = q[3]
        return pose

def main(args=None):
    rclpy.init(args=args)
    MazeNavigator()
