# Configuration

## Setup
* Config file is in `/opt/ros/indigo/setup.zsh`

**Workspace**
```
rosws init ~/workspace-name /opt/ros/indigo
```

**Sandbox**
```
mkdir ~/workspace/sandbox
rosws set ~/workspace/sandbox
source ~/workspace/setup.zsh
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

## Creating a ROS package
* ` roscreate-pkg [package_name] [depend1] [depend2] [depend3]`
* checking dependencies : `rospack depends1 [package_name]`

## Building a ROS package
* `rosmake [package]`
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
