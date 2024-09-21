import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class FirstSubscriber(Node):
    def __init__(self):
        super().__init__('first_subscriber') # Create a ROS2 node with the given name 'first_subscriber'
        self.subscription_ = self.create_subscription(String, 'topic', self.listener_callback, 10) # Create a
        # subscriber to listen for messages on the 'topic' topic
        self.subscription_ # Automatically start listening for messages when the node starts

    def listener_callback(self, sms):
        #pass
        #self.get_logger().info('sdf')
        a = f': "{sms.data}"'
        a = a.split()
        self.get_logger().info(a[1])

def main(args = None):
        rclpy.init(args = args) # Initialize ROS2
        first_subscriber = FirstSubscriber() # Create an instance of our custom ROS2 node
        rclpy.spin(first_subscriber) # loop through all the subscribers
        first_subscriber.destroy_node() # Destroy the node explicitly when done with it, otherwise it will be done
        # automatically when the garbage collector
        rclpy.shutdown() # Clean up the ROS2 node


if __name__ == '__main__':
    main()
