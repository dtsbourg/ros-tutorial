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
