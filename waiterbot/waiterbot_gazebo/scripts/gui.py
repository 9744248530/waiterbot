#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from tf.transformations import quaternion_from_euler
from actionlib_msgs.msg import GoalStatusArray
import Tkinter as tk

class WaiterGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("TurtleBot Waiter GUI")

        self.goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
        rospy.Subscriber('/move_base/status', GoalStatusArray, self.goal_status_callback)
        
        self.locations = {
            "Table 1": (.7, 2.0, 0.0),
            "Table 2": (-1, 2.0, 0.0),
            "Table 3": (-1.2, 3.2, 0.0),
            "Kitchen": (-2.0, -.4, 0.0)
        }

        self.goals = []
        self.current_goal_index = 0
        self.order_received = False
        self.goal_reached = False
        self.timer_started = False

        for location in ["Table 1", "Table 2", "Table 3"]:
            button = tk.Button(master, text=location, command=lambda loc=location: self.add_goal(loc))
            button.pack(pady=5)
        
        self.order_received_button = tk.Button(master, text="Order Received", command=self.handle_order_received)
        self.order_received_button.pack(pady=5)
        self.order_received_button.config(state=tk.DISABLED)

        self.start_button = tk.Button(master, text="Start", command=self.start_journey)
        self.start_button.pack(pady=5)

    def add_goal(self, location):
        self.goals.append(location)
        rospy.loginfo("Added goal: {}".format(location))

    def start_journey(self):
        if not self.goals:
            rospy.logwarn("No goals to visit!")
            return
        self.order_received_button.config(state=tk.NORMAL)
        self.current_goal_index = 0
        self.send_next_goal()

    def send_next_goal(self):
        if self.current_goal_index < len(self.goals):
            goal_location = self.goals[self.current_goal_index]
            self.current_goal_index += 1
            self.goal_reached = False
            self.send_goal(goal_location)
        else:
            self.return_to_kitchen()

    def handle_order_received(self):
        self.order_received = True
        if self.current_goal_index < len(self.goals):
            self.send_next_goal()
        else:
            self.return_to_kitchen()

    def goal_status_callback(self, status):
        if status.status_list and status.status_list[-1].status == 3:  # Goal reached status
            if not self.goal_reached:
                self.goal_reached = True
                self.timer_started = False  # Ensure the timer starts after reaching the goal
                if self.current_goal_index - 1 < len(self.goals):
                    rospy.loginfo("Goal reached: {}".format(self.goals[self.current_goal_index - 1]))
                self.master.after(20000, self.check_order_received)  # Start the 20-second timer

    def check_order_received(self):
        if not self.goal_reached or self.timer_started:
            return
        self.timer_started = True
        if not self.order_received:
            if self.current_goal_index < len(self.goals):
                rospy.loginfo("Order not received, moving to next goal.")
                self.send_next_goal()
            else:
                self.return_to_kitchen()
        else:
            if self.current_goal_index >= len(self.goals):
                self.return_to_kitchen()
            else:
                self.send_next_goal()

    def return_to_kitchen(self):
        rospy.loginfo("Returning to kitchen.")
        self.goals = ["Kitchen"]
        self.current_goal_index = 0
        self.send_goal("Kitchen")

    def send_goal(self, location):
        x, y, theta = self.locations[location]
        quaternion = quaternion_from_euler(0, 0, theta)
        goal = PoseStamped()
        goal.header.frame_id = "map"
        goal.pose.position.x = x
        goal.pose.position.y = y
        goal.pose.position.z = 0.0
        goal.pose.orientation.x = quaternion[0]
        goal.pose.orientation.y = quaternion[1]
        goal.pose.orientation.z = quaternion[2]
        goal.pose.orientation.w = quaternion[3]

        rospy.loginfo("Sending goal to {}: ({}, {}, {})".format(location, x, y, theta))
        self.goal_pub.publish(goal)
        self.goal_reached = False  # Reset the goal reached flag

    def reset_journey(self):
        self.goals = []
        self.current_goal_index = 0
        self.order_received_button.config(state=tk.DISABLED)
        self.order_received = False
        rospy.loginfo("Journey complete and reset.")

if __name__ == "__main__":
    rospy.init_node('turtlebot_waiter_gui', anonymous=True)
    root = tk.Tk()
    gui = WaiterGUI(root)
    root.mainloop()

