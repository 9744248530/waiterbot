^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package waiterbot_bringup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.2.6 (2022-02-24)
------------------
* add LDS-02 support
* Contributors: Will Son

1.2.5 (2020-12-30)
------------------
* No Changes

1.2.4 (2020-09-29)
------------------
* Package info updated
* Contributors: Will Son

1.2.3 (2020-03-03)
------------------
* none

1.2.2 (2019-08-20)
------------------
* none

1.2.1 (2019-08-20)
------------------
* Added waiterbot_remote.launch to waiterbot_model.launch `#389 <https://github.com/ROBOTIS-GIT/waiterbot/issues/389>`_
* Contributors: Jonathan Hechtbauer, Gilbert

1.2.0 (2019-01-22)
------------------
* none

1.1.0 (2018-07-23)
------------------
* added bringup to load multiple robot simply #251
* added argument about namespace
* updated waiterbot_diagnostic node
* updated firmware version from 1.2.0 to 1.2.2
* updated get firmware version
* updated version check function
* updated warn msg for version check
* Contributors: Darby Lim, Gilbert, Pyo

1.0.0 (2018-05-29)
------------------
* added variable to check version only once
* modified firmware version
* modified global names `#211 <https://github.com/ROBOTIS-GIT/waiterbot/issues/211>`_ from FurqanHabibi/fix_global_topic_name
* modified waiterbot_rpicamera.yaml gets camera_info_url value from the initialized calibration file
* deleted count version info msg
* merged pull request `#220 <https://github.com/ROBOTIS-GIT/waiterbot/issues/220>`_ `#212 <https://github.com/ROBOTIS-GIT/waiterbot/issues/212>`_ `#200 <https://github.com/ROBOTIS-GIT/waiterbot/issues/200>`_ `#156 <https://github.com/ROBOTIS-GIT/waiterbot/issues/156>`_ `#154 <https://github.com/ROBOTIS-GIT/waiterbot/issues/154>`_ `#153 <https://github.com/ROBOTIS-GIT/waiterbot/issues/153>`_ `#150 <https://github.com/ROBOTIS-GIT/waiterbot/issues/150>`_ `#147 <https://github.com/ROBOTIS-GIT/waiterbot/issues/147>`_ `#146 <https://github.com/ROBOTIS-GIT/waiterbot/issues/146>`_
* Contributors: Darby Lim, Leon Jung, Muhammad Furqan Habibi, Pyo

0.2.1 (2018-03-12)
------------------
* refactoring for release
* Contributors: Pyo

0.2.0 (2018-03-12)
------------------
* refactoring for release
* updated firmware version
* modified param config
* added waiterbot_rpicamera.launch for raspberry pi camera
* added waffle pi model
* added verion check function
* added diagnostics node
* added scripts for reload rules
* Contributors: Darby Lim, Gilbert, Leon Jung, Pyo

0.1.6 (2017-08-14)
------------------
* updated model.launch
* fixed typo
* fixed xacro.py deprecation
* modified file location
* Contributors: Darby Lim, Hunter L. Allen

0.1.5 (2017-05-25)
------------------
* changed the node name from hlds_laser_publisher to waiterbot_lds
* Contributors: Pyo

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
