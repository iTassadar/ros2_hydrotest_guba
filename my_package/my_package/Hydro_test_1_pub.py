import rclpy
from rclpy.node import Node
import random
from std_msgs.msg import String

class FirstPublisher(Node):
    def __init__(self):
        super().__init__('first_publisher') # Create a ROS2 node with the given name 'first_publisher'
        self.publisher_ = self.create_publisher(String, 'topic', 10) # Create a publisher to publish messages to the 'topic' topic
        self.timer_ = self.create_timer(1, self.publish_message)
        self.i = 0


    def publish_message(self):
        msg = String()
        sms = String()
        self.ran = random.randint(1, 1000)
        msg.data = f'Сейчас прошла {self.i}-я секунда' # Create a new message with a string content
        sms.data = f'{self.ran} секунд'

        #self.publisher_.publish(msg) # Publish the message to the 'topic' topic
        self.publisher_.publish(sms)  #
        self.get_logger().info(f'Publishing: "{sms.data}"') # Log the message being published
        self.i += 1


def main(args=None):
    rclpy.init(args = args) # Initialize ROS2
    first_publisher = FirstPublisher() # Create an instance of our custom ROS2 node
    rclpy.spin(first_publisher) # loop through all the publishers
    first_publisher.destroy_node() # Destroy the node explicitly when done with it, otherwise it will be done
    # automatically when the garbage collector
    rclpy.shutdown() # Clean up the ROS2 node


if __name__ == '__main__':
    main()