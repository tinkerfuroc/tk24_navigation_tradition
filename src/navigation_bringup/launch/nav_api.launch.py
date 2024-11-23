from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    compute_grasp_node = Node(
        package='ros2_grasp_position_compute',
        executable='compute_grasp_pos',
        name='compute_grasp_pos_node',
        output='screen'
        )

    client_node = Node( 
        package='nav_api',
        executable='nav_client',
        name='nav_client_node',
        output='screen'
        )

    return launch.LaunchDescription([
        compute_grasp_node,
        client_node
    ])

