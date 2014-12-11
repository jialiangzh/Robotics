#!/bin/sh -x

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

cd "/home/pi/ros_workspace/src/image_pipeline/camera_calibration"

# todo --install-layout=deb per platform
# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
/usr/bin/env \
    PYTHONPATH="/home/pi/ros_workspace/install/lib/python2.7/dist-packages:/home/pi/ros_workspace/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/pi/ros_workspace/build" \
    "/usr/bin/python" \
    "/home/pi/ros_workspace/src/image_pipeline/camera_calibration/setup.py" \
    build --build-base "/home/pi/ros_workspace/build/image_pipeline/camera_calibration" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/pi/ros_workspace/install" --install-scripts="/home/pi/ros_workspace/install/bin"
