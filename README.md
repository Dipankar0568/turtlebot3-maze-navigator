# TurtleBot3 Maze Navigator (ROS 2)

This ROS 2 project implements autonomous maze solving and navigation logic for a TurtleBot3 robot using simulation or real-world deployment.

## 📦 Packages

- `turtlebot3_maze_solver`: Implements maze-solving algorithms (e.g., right-hand rule, wall-following).
- `turtlebot3_navigator`: Controls movement, obstacle avoidance, and integration with navigation stack.

## 🛠️ Dependencies

- ROS 2 Humble/Foxy
- `turtlebot3` packages
- `rclpy` or `rclcpp` (based on your language)
- Gazebo (for simulation)

## 🚀 How to Launch

```bash
cd ~/ros2_ws
colcon build --packages-select turtlebot3_maze_solver turtlebot3_navigator
source install/setup.bash
ros2 launch turtlebot3_maze_solver maze_solver.launch.py
