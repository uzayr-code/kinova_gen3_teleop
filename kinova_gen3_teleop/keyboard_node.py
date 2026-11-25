# Imports
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import select
import sys

# Creating the Node object
class KeyboardNode(Node):

    # (1) Defines the Keyboard Node
    def __init__(self):
        super().__init__('keyboard_node')

        # (a) Subscribe to the joint states topic
        self.joint_positions = {}
        self.joint_state_subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_state_callback,
            10,
        )
        self.get_logger().info('Waiting for joint states...')

        # (b) Create a timer to check for keyboard input
        self.keyboard_timer = self.create_timer(0.05,self.check_keyboard,)


    # (2) Defines the callback function to update joint positions
    def joint_state_callback(self, msg):
        self.joint_positions = dict(zip(msg.name, msg.position))

        self.get_logger().info(
            f'Joint positions: {self.joint_positions}',
            throttle_duration_sec=2.0,
        )


    # (3) Defines the function to check for keyboard input
    def check_keyboard(self):
        ready, _, _ = select.select([sys.stdin], [], [], 0)
        if not ready:
            return
        
        key = sys.stdin.readline().strip().lower()
        if key == 'a':
            self.get_logger().info('Decrease joint 1')
        elif key == 'd':
            self.get_logger().info('Increase joint 1')
        elif key == 'q':
            self.get_logger().info('Stopping keyboard node')
            rclpy.shutdown()


# Ros communication
def main(args=None):
    rclpy.init(args=args)
    node = KeyboardNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


# Executable
if __name__ == '__main__':
    main()