# Software Overview

This folder contains the early software work for oure autonomous rover project.
Everything is still in the “baby steps” phase, so testing ideas, figuring out ROS2, and building the basics for mapping, control, and simple autonomy.

I’ve been experimenting with TurtleBot3 Burger examples to understand ROS2 movement and LIDAR workflows, but since this rover uses different hardware (Jetson nano, custom sensors), most things will be adapted or rewritten as I learn more.

This isn’t a finished system. It’s a learning project that grows as I figure things out.

# What This Will Eventually Do
- The goal is to build software that can:
- Read sensor data (IMU, LDR, wheel/motor feedback)
- Build a simple map of the environment
- Keep track of the robot’s position
- Plan paths and follow basic goals
- Run onboard on a Jetson for off-road use

Right now I’m focusing on the fundamentals:
testing motors, reading sensors, and learning the ROS2 workflow.

# Why This Repo Exists
This is a university project, a learning experience, and a place to document progress, not a polished robotics stack (yet).
I’ll keep updating things as I learn more and the rover becomes more capable.

# Folder Structure (Quick Tour)
`software/`
- `control/`:  Basic movement tests + motor control scripts
- `mapping/`: First attempts at mapping + simple room visualization  (work in progress)
- `mission_planning/`: Early path-planning experiments  (work in progress)
- `tests/`: Small scripts for checking sensors, signals, and debugging (work in progress)

Each section has a small README that explains what’s inside. Though for now theres not much in them.

# Next Steps
- Try simple SLAM 
- Improve mapping and sensor fusion
- Clean up the structure as the project grows
- Add simulation once the real robot becomes more predictable

# Problems
What to use for a LIDAR (This section is explored more in detail in the `hardware` -> `sensors` part):
- A 3D one is expensive
- could build one that goes up and down
- then again could use a camera and do some basic object recognition
- need to get basic controls working fast before can start integrating sensors

# Updates
- Jetson nano is setup
- ros2 workplase is setup
- basic controlls work. can drive it around on computer.
- working on URDF



---
# Basic data flow idea
<img width="1500" height="2000" alt="image" src="https://github.com/user-attachments/assets/4af0bf23-be87-402e-9e69-5190418e61b9" />
