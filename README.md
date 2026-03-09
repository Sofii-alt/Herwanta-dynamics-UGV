#   Dual - Use UGV system

Welcome to our student rover project! This is a small-group work-in-progress autonomous ground robot that can map its surroundings, navigate, and has an end-effector/marking system on top.

The aim is to combine mechanical design, control systems, mapping, and system integration, while learning real-world robotics skills.
Note: Everyone contributes a bit across the teams since this is a small student project.

# Robot showcase
<img width="993" height="555" alt="image" src="https://github.com/Sofii-alt/Herwanta-dynamics-UGV/blob/main/docs/design_sketches/2D_drawings/HiisiProto2-2.png" />
A preliminary sketch for the robot without the dual use functionality yet.
<img width="993" height="555" alt="image" src="https://github.com/Sofii-alt/Herwanta-dynamics-UGV/blob/main/docs/Gallery/UprightAssembly.jpg" />
An upright assembly.
<img width="993" height="555" alt="image" src="https://github.com/Sofii-alt/Herwanta-dynamics-UGV/blob/main/docs/Gallery/FittingTemporaryAxels1.jpg" />
Tires installed with failed 3D prints for visual formatting.

---
# Project Goals
- Develop a rover that can map rooms or outdoor areas using LIDAR, wheel encoders, and IMU.
- Implement basic navigation and motor control using Nvidia Jetson
- Integrate an end-effector for pointing at targets.
- Learn and practice mechanical, electrical, and software integration.


# Repository Structure
`design_sketches/`   -> mechanical drafts, CAD files, 3D renderings  
`hardware/`          -> motors, batteries, sensors, wiring diagrams, calculations  
`software/`          -> control scripts, ROS2 nodes, mapping, navigation  
`tests/`             -> logs, LIDAR data, sensor diagnostics, experiments  


Team Structure
---


# Team 1: Mechanical

Members:

| Aatu | 

| Veeti |

Responsibilities: 
- Chassis construction
- Motor selection and installation
- Encoders, battery mounting, electronics layout
- Mechanical stability and durability
- Electrical wiring



# Team 2: Software 

Members:

| Leo | 

| Sofia | 

Responsibilities:
- End effector system
- Navigation stack and communication systems
- Motor control and sensor fusion
- System-wide testing and integration
- Github upkeep
---

# Current Progress
- Mechanical: Physical lasercut frames are assembled along with motors, mounted to the V-slot aluminium frames. Motor operation was tested and stallcurrent was approximated. Due to the power of the motors this was a high imagination process as sufficient counter torque could not be applied with the tools in hand.
- Electrical: motor and battery calculations ready. An electrical box was installed for drivers (BTS7960) and a sub controller (ESP32). Wiring is currently under revision for safety reasons.

