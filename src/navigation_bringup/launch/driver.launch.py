#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2021, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node


def generate_launch_description():
    tracer_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([FindPackageShare('tracer_base'), 'launch', 'tracer_base.launch.py'])),
        launch_arguments={}.items(),
    )

    livox_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([FindPackageShare('livox_ros_driver2'), 'launch', 'laserscan_MID360_launch.py'])),
        launch_arguments={}.items(),
    )

    orbbec_tf = Node(
            package='tf2_ros',
            namespace = 'scan_to_map',
            executable='static_transform_publisher',
            arguments= ["0", "0", "1.4", "0", "0.42", "0", "base_link", "camera_link"]
        )

    rviz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([FindPackageShare('navigation_bringup'), 'launch', 'rviz_launch.py'])),
        launch_arguments={}.items(),
    )

    kissicp_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([FindPackageShare('kiss_icp'), 'launch', 'odometry.launch.py'])),
        launch_arguments={}.items(),
    )
    
    return LaunchDescription([
        tracer_launch,
        livox_launch,
        orbbec_tf,
        kissicp_launch,
        rviz_launch
    ])
