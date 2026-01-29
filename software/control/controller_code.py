# PLACEHOLDER
# controller_code


# TODO
## file where spesify joints
## file for parameter rates
## filer for sensor data and a place that compares them

<robot
  <Ros2 control name="SomeSystem" type="system"

    <hardware>
      # Tels the code how to talk to talk to the gazebo (hardware phase)
      <plugin><gazebo_ros2_control/SomeSystem</plugin>
    <hardware>
    # What joints it controlls

    <joint name="wheel_1">
      # needed interfaces
      <command interface name="velcosity">
        <param name="min"> NUM </param>
        <param name="max"> NUM </param>
      <command_interface>
      <state interface name="velcosity"/>
      <state interface name="position"/>      
    </joint>

     <joint name="wheel_2">
      # needed interfaces
      <command interface name="velcosity">
        <param name="min"> NUM </param>
        <param name="max"> NUM </param>
      <command_interface>
      <state interface name="velcosity"/>
      <state interface name="position"/>      
    </joint>

  </ros2_control>

  <gazebo>
    # has its own controller manager
    <plugin name="gazebo_ros2_control" filename=lingazebo_ros2_control.so">
      <parameters>$(find THE_FILE_THAT_HAS_THE_CONTENTS_OF_ABOVE.yaml<
      # make new file "controll manager"
      #  controller_manager:
      #    ros_parameters:
      #      update_rate: 30
      #      use_sim_time: true
      # name controller and give it a type
      #      diff_count:
      #        type: diff_drive_controller/diffDriveController
      # joint state needs to be published
      #      joint_broad:
      #        type: joint_state_broadcaster/JointStateBroadcaster
    </plugin> 
      
  </gazebo>
    
</robot>
