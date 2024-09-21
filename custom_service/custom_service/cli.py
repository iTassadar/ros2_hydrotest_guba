import sys
from tutorial_interfaces.srv import Aaa
import rclpy
from rclpy.node import Node

class LengthClientAsync(Node):

    def __init__(self):
        super().__init__('length_client_async')
        self.cli = self.create_client(Aaa, 'aaa')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.req = Aaa.Request()

    def send_request(self, strg):
        self.req.str = strg
        self.future = self.cli.call_async(self.req)

def main():
    rclpy.init()

    if len(sys.argv) < 2:
        print("Usage: ros2 run <your_package_name> client <your_string>")
        return

    input_str = sys.argv[1]
    length_client = LengthClientAsync()  # Создание экземпляра клиента

    length_client.send_request(input_str)  # Отправка запроса с введенной строкой

    while rclpy.ok():
        rclpy.spin_once(length_client)
        if length_client.future.done():
            try:
                response = length_client.future.result()
            except Exception as e:
                length_client.get_logger().info(f'Service call failed: {e}')
            else:
                length_client.get_logger().info(f'Response: {response.len}')
            break

    length_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
