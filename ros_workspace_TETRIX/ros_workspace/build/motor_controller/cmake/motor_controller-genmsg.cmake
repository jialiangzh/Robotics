# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "motor_controller: 1 messages, 0 services")

set(MSG_I_FLAGS "-Imotor_controller:/home/pi/ros_workspace/src/motor_controller/msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

#better way to handle this?
set (ALL_GEN_OUTPUT_FILES_cpp "")

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(motor_controller
  /home/pi/ros_workspace/src/motor_controller/msg/MotorCommand.msg
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/motor_controller
)

### Generating Services

### Generating Module File
_generate_module_cpp(motor_controller
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/motor_controller
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(motor_controller_gencpp ALL
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(motor_controller
  /home/pi/ros_workspace/src/motor_controller/msg/MotorCommand.msg
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/motor_controller
)

### Generating Services

### Generating Module File
_generate_module_lisp(motor_controller
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/motor_controller
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(motor_controller_genlisp ALL
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(motor_controller
  /home/pi/ros_workspace/src/motor_controller/msg/MotorCommand.msg
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/motor_controller
)

### Generating Services

### Generating Module File
_generate_module_py(motor_controller
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/motor_controller
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(motor_controller_genpy ALL
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)


debug_message(2 "motor_controller: Iflags=${MSG_I_FLAGS}")


if(gencpp_INSTALL_DIR)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/motor_controller
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()

if(genlisp_INSTALL_DIR)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/motor_controller
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()

if(genpy_INSTALL_DIR)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/motor_controller\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/motor_controller
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
