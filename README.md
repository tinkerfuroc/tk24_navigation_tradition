# Dependecies

```sh
sudo apt install ros-humble-pointcloud-to-laserscan
```

map.yaml 
bringup.launch line 100
```
    bringup_dir, 'maps', 'xlab.yaml'
```

launch 
```
ros2 launch navigation_bringup driver.launch.py
ros2 launch navigation_bringup bringup_launch.py
start up
give 2d pose estimate
ros2 launch navigation_bringup nav_api.launch.py
```

get pose in map
```
ros2 topic echo /goal_pose
send 2d pose in rviz
```

