# Robot Project System Overview

This project aims to build a mobile robot capable of mapping its environment and performing basic autonomous navigation.

## Components

- **LIDAR sensor:** Measures distances to obstacles and maps the environment.
- **Motors & Encoders:** Move the robot and provide wheel odometry.
- **Battery pack:** Powers the robot.
- **Controller board:** Runs ArduPilot/ROS and communicates with sensors.
- **Mission planning software:** Receives map data and sends navigation commands.

## Data flow

