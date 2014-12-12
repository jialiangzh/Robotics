#Author: Aaron Bestick
#Date: Nov 4th, 2014

#This script installs the full version of ROS Hydro
#as well as some other software that's useful for EE125, like 
#up-to-date versions of NumPy, SciPy and the Baxter SDK.
#It assumes you're using a clean install of Ubuntu 12.04.
#No guarantees about its behavior if you use it on other 
#versions/distros!

#CAUTION: since you're running this as root, it has the
#potential to overwrite important files if you do things wrong!
#In particular, be sure the LINUX_USER and WORKSPACE variables
#are set correctly for your install. Backing up your important 
#data before you make big configuration changes is always 
#wise as well :)

#Steps:
#1) Set the four config variables below and save your changes
#2) Run the script as root (e.g. sudo bash ros_setup_new.bash)
#   You can also log the setup info to a file, for troubleshooting if 
#   anything goes wrong (e.g. sudo bash ros_setup_new.bash > setup_log.txt)
#3) Wait until it's all done and you're ready to go! (the install
#   takes a while - about 30 minutes on a computer with a fast internet
#   connection)

#SET THESE VARIABLES BEFORE RUNNING-------------------------
#Which user should ROS be installed for?
LINUX_USER=saasbook

#The name of your default ROS workspace (under the selected user's home directory)
WORKSPACE=ros_workspace

#Install the latest versions of NumPy and SciPy
NUMPY_SCIPY=true

#Install the Baxter SDK and MoveIt
BAXTER=false

#DON'T CHANGE ANYTHING BELOW HERE---------------------------

#Add the ROS repos to the sources list and set up the keys
echo "Adding repos..."
sh -c 'echo "deb http://packages.ros.org/ros/ubuntu precise main" > /etc/apt/sources.list.d/ros-latest.list'
wget http://packages.ros.org/ros.key -O - | apt-key add -
apt-get update

#Install ROS and some additional ROS libraries
echo "Installing ROS..."
echo "hddtemp hddtemp/daemon boolean false" | debconf-set-selections
apt-get install -y libx11-6
apt-get install -y ros-hydro-desktop-full
apt-get install -y ros-hydro-usb-cam ros-hydro-image-view
rosdep init
apt-get install -y python-rosinstall git-core python-argparse python-wstool python-vcstools python-rosdep ros-hydro-control-msgs ros-hydro-joystick-drivers

#Make the ROS workspace
echo "Setting up the ROS workspace..."
source /opt/ros/hydro/setup.bash
mkdir -p /home/$LINUX_USER/$WORKSPACE/src
cd /home/$LINUX_USER/$WORKSPACE/src
catkin_init_workspace
cd ..
catkin_make
echo "source /opt/ros/hydro/setup.bash" >> /home/$LINUX_USER/.bashrc
echo "source /home/$LINUX_USER/$WORKSPACE/devel/setup.bash" >> /home/$LINUX_USER/.bashrc
source /home/$LINUX_USER/$WORKSPACE/devel/setup.bash

#Install the Baxter SDK and MoveIt
if $BAXTER ; then
	echo "Installing the Baxter SDK"
	cd src
	mkdir baxter_sdk
	cd baxter_sdk
	wstool init .
	wstool merge https://raw.githubusercontent.com/RethinkRobotics/baxter/master/baxter_sdk.rosinstall
	wstool update
	cd ../..
	catkin_make

	echo "Installing MoveIt"
	cd src
	mkdir baxter_misc
	cd baxter_misc
	git clone https://github.com/ros-planning/moveit_robots.git
	apt-get install -y ros-hydro-moveit-full
	cd ../..
	catkin_make
fi

#Install and build NumPy and SciPy
if $NUMPY_SCIPY ; then
	echo "Installing NumPy, SciPy, and Matplotlib"
	apt-get install -y python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
	apt-get install -y gfortran libopenblas-dev liblapack-dev python-pip
	pip install numpy --upgrade
	pip install scipy --upgrade
fi

#Set permissions
chown -R $LINUX_USER /home/$LINUX_USER/$WORKSPACE
chgrp -R $LINUX_USER /home/$LINUX_USER/$WORKSPACE
chmod -R 755 /home/$LINUX_USER/$WORKSPACE
