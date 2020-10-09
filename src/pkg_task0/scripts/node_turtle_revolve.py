#!/usr/bin/env python

# Import the necessory packages
from __future__ import print_function # import the future updates of python
from geometry_msgs.msg import Twist # import the Package, to publish x,y,z values of angular and linear velocities
from turtlesim.msg import Pose # import the package to handle the callback, to know the x, y, and theta values
import rospy # import the package which is very important in programming Robots in python using ROS

linear_velocitiy = [0.5, 0.0, 0.0] # provide linear velocities in x,y,z direction
angular_velocity = [0.0, 0.0, 0.8] # provide angular velocities in x,y,z direction

node_name = "node_turtle_revolve" # Node name
publish_name = "turtle1/cmd_vel" # Publish topic name
subscribe_name = "turtle1/pose" # subscribe topic name

# Create a class, which has the methods such as __init__ which initialises the program based on the primary constructor
class TurtleRobot:
    # Constructor and its parameters
    def __init__( self, linear_x, linear_y, linear_z, angular_x, angular_y, angular_z, node_name, publisher_name, subscriber_name):
        # Setup the Linear velocities of x,y,z
        self.lin_x, self.lin_y, self.lin_z = linear_x, linear_y, linear_z
        # Setup the Angular velocity of x,y,z
        self.ang_x, self.ang_y, self.ang_z = angular_x, angular_y, angular_z
        # Initialse the Node with the name provided
        rospy.init_node(node_name, anonymous=True)
        # Create a publisher with the respective topic given
        self.velocity_publisher = rospy.Publisher(publisher_name, Twist, queue_size=10)
        # Create a Subscriber with the respective topic given
        rospy.Subscriber(subscriber_name, Pose, self.pose_callback)
        # Log the info on the screen
        rospy.loginfo("Instance created successfully")

    # Method to use the callback function when the data is subscribed, and the message is recieved
    def pose_callback(self, msg):
        # Format the handler message msg.theta to %.2f so that the completion of the circle can be determined
        temp_msg = float("{:.2f}".format(msg.theta))
        # If value temp_msg == "-0.02" means that, the turtle robot has completed its one rotation successfully
        if str(temp_msg) == "-0.01":
            self.lin_x = 0.0 # Set the params to 0.0, so that there will be no linear motion over x axis
            self.ang_z = 0.0 # Set the params to 0.0, so that there will be no angular motion over z axis


    def begin(self):
        # Begin to publish the message
        while not rospy.is_shutdown():
            # Create the Twist Object
            vel_msg = Twist()
            # Copy the Linear velocity values to the object
            vel_msg.linear.x, vel_msg.linear.y, vel_msg.linear.z = self.lin_x, self.lin_y, self.lin_z
            # Copy the Angular velocity values to the object
            vel_msg.angular.x, vel_msg.angular.y, vel_msg.angular.z = self.ang_x, self.ang_y, self.ang_z
            # Publish the message
            self.velocity_publisher.publish(vel_msg)



# Run the Main program only if __name__ is __main__
if __name__=="__main__":
    # Try to tun the Program in try catch block
    try:
        # Create a Instance for the class TurtleRobot
        instance = TurtleRobot(linear_velocitiy[0], linear_velocitiy[1], linear_velocitiy[2], angular_velocity[0], angular_velocity[1], angular_velocity[2], node_name, publish_name, subscribe_name)
        # Run the instance
        instance.begin()

    except rospy.ROSInterruptException:
        # Exception raises, in order to handle the exception which occurs due to Keyboard Interrupt
        pass # Do nothing
