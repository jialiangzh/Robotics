
#SET THESE VARIABLES BEFORE RUNNING-------------------------
#Which user should ROS be installed for?
LINUX_USER=saasbook

#The name of your default ROS workspace (under the selected user's home directory)
WORKSPACE=ros_workspace

#Install the latest versions of NumPy and SciPy
NUMPY_SCIPY=true

#Install the Baxter SDK and MoveIt
BAXTER=false


#Set permissions
chown -R saasbook /home/ubuntu/ros_workspace
chgrp -R saasbook /home/ubuntu/ros_workspace
chmod -R 755 /home/ubuntu/ros_workspace
