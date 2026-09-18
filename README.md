# RobotiqueStudio Labs | Autonomous Control & Simulation

This repository contains autonomous navigation algorithms and high-fidelity simulation environments developed by **RobotiqueStudio Labs (RSL)**.

## 🛠️ Technologies & Tools
- **Framework:** ROS 2 (Humble / Jazzy)
- **Simulators:** Webots / Gazebo
- **Languages:** Python / C++
- **Control Theory:** PID / Path Planning / Obstacle Avoidance

## 📂 Project Structure
- `/worlds`: Contains `.wbt` (Webots) or `.world` (Gazebo) environment configurations.
- `/scripts`: Custom control loops, node setups, and kinematic model algorithms.

## 🚀 How to Run the Simulation
1. Clone this repository in your ROS 2 workspace.
2. Launch the simulation environment:
   ```bash
   # Example command to launch your simulator
   webots worlds/ma_simulation.wbt
   ```
3. Run the autonomous control node:
   ```bash
   python3 scripts/pid_controller.py
   ```
