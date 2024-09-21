from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='custom_service',
            executable='service',
            name='serv',
            output='screen',
        ),
        Node(
            package='custom_service',
            executable='client',
            name='cli',
            output='screen',
            arguments=['ААААА аааа'],
        ),
        Node(
            package='my_package',
            executable='talker',
            name='Hydro_test_1_pub',
            output='screen',
        ),
        Node(
            package='my_package',
            executable='listener',
            name='Hydro_test_1_sub',
            output='screen',
        )
    ])
