# Configuration

## Setup
* Config file is in `/opt/ros/indigo/setup.zsh`

**Workspace**
```
catkin_init_workspace
```

**Sandbox**
```
source devel/setup.zsh
```

## ROS FS
### Overview
* Packages : librairies, tools, execs, ...
* Manifests : package description
* Stacks : collection of packages

### Tools
* `rospack find [package_name]`
* `rosstack find [package_name]`
* `roscd [locationname[/subdir]]`
* `rosls [locationname[/subdir]]`
* `roscp [package_name] [file_to_copy_path] [copy_path]`

## Creating a ROS package
* ` catkin_create-pkg [package_name] [depend1] [depend2] [depend3]`
* checking dependencies : `rospack depends1 [package_name]`

## Building a ROS package
* `catkin_make [make_targets]`
  * `catkin_make` will build all packages in src (run from ws)
  * `catkin_make install`
* `rosdep [package]` installs package dependencies

# ROS Basics

## ROS Nodes
### Definitions
* node = executable within a ROS package
* messages = ROS data type for subscribing or publishing to a topic
* topics = where nodes publish messages
* master = name service for ROS
* rosout = ROS stdout
* roscore = Master + rosout + parameter server

### Running
* `roscore` (use to start ROS stack)
* `rosnode list` (shows active nodes)
* `rosnode info /node_name`
* `rosrun package_name node_name`
* `rosnode clean` (clean node list)
* `rosnode ping node_name`

## ROS Topics
* nodes can publish to Topics
* nodes can subscribe to topics
* `rosrun rqt_graph rqt_graph` show topic graph
* `rosrun rqt_plot rqt_plot` plots
* `rostopic [cmd] [args]` info about topics
  * `rostopic echo [topic]` show data being published to the topic
  * `rostopic list -v` show all topics subscribed / published to
  * `rostopic type [topic]` show message type (`rosmsg show [message_name]` for more info)
  * publish `rostopic pub [topic] [msg_type] [args]` (-n to publish n messages, -r for 1 Hz refresh)
  * publish rate `rostopic hz [topic]`

## ROS Services
* `rosservice list` print information about active services
* `rosservice call` call the service with the provided args
* `rosservice type` print service type
* `rosservice find` find services by service type
* `rosservice uri` print service ROSRPC uri

## ROS Parameter server
* use `rosparam` to store and manipulate data (`set`, `get`, `load`, `dump`, `delete`, `list`)

## ROS tooling
### Logging
* `rqt_console` attaches to the logging framework to display output from nodes
* `rqt_logger_level` change the verbosity level

### Running
* `roslaunch [package] [filename.launch]` launches nodes as specified in launch file

### Editing
* `rosed [package_name] [filename]` allows editing a file within a package without specifying the full path

## ROS message-passing
Note : don't forget to build the project after adding msg / srv : `catkin_make`
### msg
* description of ROS message
* stored in `msg/Filename.msg`
* in `CMakeLists.txt`
  * add `message_generation`
  * make sure message runtime dependency is exported
  * uncomment `add_message_files` and add `.msg` files
  * uncomment `generate_messages()` and add all dependencies
* Types
  * int8, int16, int32, int64 (plus uint*)
  * float32, float64
  * string
  * time, duration
  * other msg files
  * variable-length array[] and fixed-length array[C]
  * Header (timestamp + frame info)

```
Header header
string child_frame_id
geometry_msgs/PoseWithCovariance pose
geometry_msgs/TwistWithCovariance twist
```

### srv
* decription of a service
* stored in `srv/Filename.srv`
* in `CMakeLists.txt`
  * add `message_generation` to `find_package`
  * uncomment `add_service_files()` and add `.srv` files
* in `package.xml` uncomment :
```
<build_depend>message_generation</build_depend>
 <run_depend>message_runtime</run_depend>
```

* `rossrv show [service]` to get info

```
int64 A #requests
int64 B
---
int64 Sum #response
```

## ROS data records

* run the services (`roscore; rosrun [topic] [node]`)
* `rostopic list -v` : examine the list of topics
* `rosbag record` record (note: inside `/bagfiles/bagfile.bag`)
  * `-a` record all topics
  * `-O subset <param_names>` record a subset (note: in file `subset.bag`)
* `rosbag info <bagfile>` to get info
* `rosbag play <bagfile>` to replay data (note: node needs to be running)
  * `-r <rate>` replay at a different rate
  * `-s <duration>` start replay at a different time

## ROS Debugging

* `roswtf`
