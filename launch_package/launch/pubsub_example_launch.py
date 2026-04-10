from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    """Launch multiple nodes, function name must same for other launch files"""

    # Create a launch description
    ld = LaunchDescription()
    nodes = []

    # Publisher node
    nodes.append(Node(
        package='cpp_pkg',
        executable='publisher_with_params',
        namespace='talkie',
        name='publisher',
        parameters=[{
            'message': 'Ceejay here!',
            'timer_period': 2.0,
        }]
    ))

    # Subscriber node 1
    nodes.append(Node(
        package='py_pkg',
        executable='minimal_subscriber',
        name='subscriber_1',
    ))

    # Subscriber node 2
    nodes.append(Node(
        package='py_pkg',
        executable='minimal_subscriber',
        namespace='talkie',
        name='subscriber_2',
    ))

    # Subscriber node 3
    nodes.append(Node(
        package='cpp_pkg',
        executable='minimal_subscriber',
        namespace='talkie',
        name='subscriber_3',
    ))

    # Add nodes to launch description
    for node in nodes:
        ld.add_action(node)

    return ld
