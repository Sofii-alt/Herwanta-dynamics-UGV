# Sensors Folder

This folder contains proposals, ideas, and considerations for sensors.

## Possible Components

### Lidar and Sensors Thoughts
- High-end lidar is an option but expensive.
- Could combine a 2D lidar with a camera as a more budget-friendly setup.

### 2D Lidar
- Detection range: ~10 meters.
- Could potentially build a "3D" lidar by mounting it on a motor.

#### Problems and Considerations
- Will the feed be stable?
- Can the robot reliably measure distance/optical info?
- Adding a camera with machine vision:
  - Could stabilize readings by comparing camera data to lidar data.
  - Learning machine vision is manageable but will take time.
  - Camera and lidar may need padding/protection.
  - Might require machine learning just to compare datasets.

#### Terrain and Environmental Issues
- Forests and rough terrain create new challenges:
  - Readings will sway with uneven ground.
  - Sensors might take hits. padding/protection needed.
  - Detecting if the robot is stuck vs. just stopped:
    - Compare sensor data with wheel movement: if all wheels move, probably not stuck.
    - Try moving slightly and see if readings change.
    - No wheel encoders available; maybe use lasers pointing at the ground.
      - Works on smooth surfaces but tricky on rough terrain.
      - Could multiple lasers help?

### General Conclusions
- Multiple components need to compare data to each other.
- Could slow down main code optimization required.
- Unsure if a Raspberry Pi 5 is enough.
- Might need separate microchips to handle sensor comparison.


### TODO
- Maby research how mars rovers do autonomous sensing
- Ask around about it
