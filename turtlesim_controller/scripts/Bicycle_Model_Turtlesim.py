#!/usr/bin/env python3
import rospy
import math
import time
from yaml import load
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


def Timer_Callback(event):
    print("Simulation has ended")
    rospy.signal_shutdown('Simulation has ended')


def pose_callback(pose_msg:Pose):
    global x, y, theta
    x = pose_msg.x 
    y = pose_msg.y 
    theta = pose_msg.theta 

    
def Simulate_Bicycle_Model(v, lr, lf, Delta, SteeringControl):
    global Beta

    rate = rospy.Rate(1)
    rospy.Timer(rospy.Duration(T), callback = Timer_Callback)

    msg = Twist()

    if SteeringControl == 1:
        Beta = math.atan2( lr * math.tan(Delta), (lr+lf) )
        Theta = ( v/(lr + lf) ) * math.cos(Beta) * math.tan(Delta)
        Vx = v * math.cos(theta + Beta)
        Vy = v * math.sin(theta + Beta)

    elif SteeringControl == 0:
        Beta = math.atan2( lf, ( (lr+lf) * math.tan(Delta) ) )
        Theta = ( (v * math.cos(Beta)) / ((lr + lf) * math.tan(Delta) ) )
        Vx = v * math.cos(Beta + theta)
        Vy = v * math.cos(Beta + theta)

    msg.linear.x = Vx
    msg.linear.y = Vy
    msg.angular.z = Theta
    
    while not rospy.is_shutdown(): 
        pub.publish(msg) 
        rate.sleep() 
    

if __name__ == "__main__":

        rospy.init_node("GBicycle_Model_Simulator")
        pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size =10)
        sub = rospy.Subscriber("/turtle1/pose", Pose, callback = pose_callback)
        
        T = int(input("Please enter desired Time of Motion: "))
        SteeringControl = int(input("For Front Steering choose 1 and for Back Steering choose 0: "))
        v = float(input("Please input linear velocity: "))
        DeltaDegree = float(input("Please enter Steering angle: "))
        pi = 22/7
        Delta = (DeltaDegree * pi ) / 180 

        file = open( '/home/esraaa/catkin_ws/src/turtlesim_controller/Config/Bicycle_Params.yaml', 'r')
        yamlfile = load(file)
        file.close()
        
        lr = rospy.get_param('lr')
        lf = rospy.get_param('lf')
       
        rospy.loginfo("Simulation has started")
        Simulate_Bicycle_Model(v, lr, lf, Delta, SteeringControl)
        


