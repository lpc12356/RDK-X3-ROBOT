from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    node1 = Node(
        package='joy',
        executable='joy_node',
    )

    node2 = Node(
        package='yahboomcar_ctrl',
        executable='yahboom_joy',
    )
    return LaunchDescription([node1, node2])
