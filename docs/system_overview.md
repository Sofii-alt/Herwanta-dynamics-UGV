# Robot Project System Overview

This project aims to build a mobile robot capable of mapping its environment and performing basic autonomous navigation.

## Components

- **LIDAR sensor:** Measures distances to obstacles and maps the environment.
- **Motors & Encoders:** Move the robot and provide wheel odometry.
- **Battery pack:** Powers the robot.
- **Controller board:** Runs ArduPilot/ROS and communicates with sensors.
- **Mission planning software:** Receives map data and sends navigation commands.
- **Raspbery Pi 5
- (Pixhawk removed)

## Data flow
<img width="1500" height="2000" alt="image" src="https://github.com/user-attachments/assets/6e52783d-2043-48f8-975f-bbfd57be01b6" />



## Goals
- Step 1: Remote control and simple sensor visualization
- Step 2: Room mapping and localization
- Step 3: Autonomous navigation with planned waypoints


