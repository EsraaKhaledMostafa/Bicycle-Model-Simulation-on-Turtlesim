# Bicycle-Model-Simulation-on-Turtlesim
## Description
It's a Package containing more than one project to control a turtle in turtlesim simulator.
Here the focus is on the Bicycle Model Simulation project.

**Bicycle_Model_Turtlesim.py**
> I've derived the kinematics of the Bicycle Model equations in both cases: forward and backward steering and simulated the results in turtlesim.
The user can input the velocity, the time of simulation, and the steering angle and also choose front steering or back steering and thus can see the result of these numbers.

## How to install and work with project 
- You should be familiar with Ubuntu and ROS.
- You can download the full package and put it in your workspace.
- You should then open the terminal and go to the directory scripts inside the package where you will find the python file of this project named: "Bicycle_Model_Turtlesim.py".

- **Hint** For Bicycle_Model_Turtlesim you could run it with roslaunch command since I've made a launch file that runs turtlesim,the code file and the parameter file. You can find it in launch folder named: "Bicycle_Model.launch". Also the length from the center of the bicycle to both the front wheel and rear wheel are given in a yaml file and sent as parameters in the code such that you can easily change there values from the yaml file.

## See Working Project
[View video](https://drive.google.com/file/d/14UHkzB7qtApBZEqQPe7GyxESPiZOJW6C/view?usp=sharing)
