# Kinova Gen3 Teleop

I'm building a ROS 2 package to control a Kinova Gen3 arm in Gazebo. The first version will use a keyboard to move the gripper. I'll then add a basket to the scene and use it to test whether the arm can reach a target without entering the space around the basket.

The simulation uses ROS 2 Jazzy, Gazebo Harmonic, and Kinova's [`ros2_kortex`](https://github.com/Kinovarobotics/ros2_kortex) packages for the robot model and controllers.

## Project goals

1. **Keyboard control.** Write a Python node that turns keypresses into small movements of the gripper.
2. **Basket avoidance.** Add a basket in Gazebo and mark its full volume as a collision object in MoveIt. Test that the arm can move around the basket when a route exists and rejects targets inside it.
3. **VR integration.** Use a tracked VR controller to set the gripper's target pose. The goal is to keep the same collision checks so the arm can still be guided around the basket.
