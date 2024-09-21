from tutorial_interfaces.srv import Aaa
import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(Aaa, 'aaa', self.aaa_callback)

    def aaa_callback(self, request, response):
        response.len = len(request.str)
        self.get_logger().info(
            f'Incoming request: {request.str}, Length: {response.len}')

        return response


def main():
    rclpy.init()
    minimal_service = MinimalService()

    try:
        rclpy.spin(minimal_service)
    except KeyboardInterrupt:
        minimal_service.get_logger().info('Shutting down service due to interrupt...')
    finally:
        minimal_service.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()