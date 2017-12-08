#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class RaceSolver(object):
	def __init__(self):
		rospy.loginfo("Initialising solver node..")
		self.laserscan_sub = rospy.Subscriber('/robot/base_scan', LaserScan, self.laser_cb, queue_size=1)
		self.velocity_pub = rospy.Publisher('/robot/cmd_vel', Twist, queue_size=1)
		self.laser_data= None
		rospy.sleep(5.0)
		rospy.loginfo("all objects created...")


	def laser_cb(self, data):
		self.laser_data = data



	def do_work(self):
		velocity = Twist()
		velocity.linear.x = 1.0
		velocity.linear.y = 0.0

		velocity.angular.z =  1.0
		rospy.loginfo("sending velocity....")
		self.velocity_pub.publish(velocity)

	def run(self):
		r = rospy.Rate(10)
		while not rospy.is_shutdown():
			self.do_work()
			r.sleep() 






if __name__ =='__main__':
	rospy.init_node('uml_solver')
	solver = RaceSolver()
	solver.run()