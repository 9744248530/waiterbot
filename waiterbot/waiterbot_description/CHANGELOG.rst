^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package waiterbot_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.2.6 (2022-02-24)
------------------
* none

1.2.5 (2020-12-30)
------------------
* Rectify IMU update rate to 0 on Gazebo
* Contributors: PinkDraconian

1.2.4 (2020-09-29)
------------------
* Package info updated
* Contributors: Will Son

1.2.3 (2020-03-03)
------------------
* Updated inertial data in waiterbot_waffle_for_open_manipulator.urdf.xacro, waiterbot_waffle_pi_for_open_manipulator.urdf.xacro
* Added waiterbot_manipulation_slam.launch for waiterbot SLAM with OpenMANIPULATOR
* Contributors: Ryan Shim, Will Son

1.2.2 (2019-08-20)
------------------
* none

1.2.1 (2019-08-20)
------------------
* none

1.2.0 (2019-01-22)
------------------
* none

1.1.0 (2018-07-23)
------------------
* added bringup to load multiple robot simply #251
* added odometrySource
* modified camera topic name
* modified base_scan update_rate and add param on diff_drive #258
* modified the laser scanner update_rate in the gazebo xacro files #258
* modified origin of collision in Waffle URDF
* Contributors: Darby Lim, Gilbert, shtseng, Pyo

1.0.0 (2018-05-29)
------------------
* added frameName for imu on gazebo (however, there is no effect.)
* modified robot names
* modified range of lidar, lidar position, scan param
* modified camera position and fixed slip bug
* modified waffle_pi stl files
* merged pull request `#220 <https://github.com/ROBOTIS-GIT/waiterbot/issues/220>`_ `#212 <https://github.com/ROBOTIS-GIT/waiterbot/issues/212>`_ `#200 <https://github.com/ROBOTIS-GIT/waiterbot/issues/200>`_ `#155 <https://github.com/ROBOTIS-GIT/waiterbot/issues/155>`_ `#154 <https://github.com/ROBOTIS-GIT/waiterbot/issues/154>`_ `#153 <https://github.com/ROBOTIS-GIT/waiterbot/issues/153>`_ `#147 <https://github.com/ROBOTIS-GIT/waiterbot/issues/147>`_ `#146 <https://github.com/ROBOTIS-GIT/waiterbot/issues/146>`_
* Contributors: Darby Lim, Pyo

0.2.1 (2018-03-14)
------------------
* refactoring for release
* Contributors: Pyo

0.2.0 (2018-03-12)
------------------
* added waffle pi model (urdf and gazebo)
* modified topic of gazebo plugin 
* refactoring for release
* modified r200 tf tree
* modified gazebo imu link
* Contributors: Darby Lim, Pyo

0.1.6 (2017-08-14)
------------------
* modified models
* fixed xacro.py deprecation
* updated IMU link
* updated gazebo config
* Contributors: Darby Lim, Hunter L. Allen

0.1.5 (2017-05-25)
------------------
* updated waiterbot waffle URDF
* Contributors: Darby Lim

0.1.4 (2017-05-23)
------------------
* modified launch file name
* added teleop package
* Contributors: Darby Lim

0.1.3 (2017-04-24)
------------------
* modified the package information for release
* modified SLAM param
* modified the description, authors, depend option and delete the core package
* modified the turtlebot bringup files
* modified pkg setting for waiterbot_core
* modified the navigation package and waiterbot node for demo
* modified the wheel speed gain
* added Intel RealSense R200
* added LDS sensor
* Contributors: Darby Lim, Pyo
