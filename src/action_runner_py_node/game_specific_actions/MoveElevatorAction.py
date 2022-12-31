from action_runner_py_node.default_actions.Action import Action
from ck_ros_msgs_node.msg import Elevator_Control, Elevator_Status
import rospy
from frc_robot_utilities_py_node.SubsystemController import SubsystemController
from ck_utilities_py_node.ckmath import *

class MoveElevatorAction(Action):
    elevator_subsystem = SubsystemController[Elevator_Control, Elevator_Status]('ElevatorControl', Elevator_Control, 'ElevatorStatus', Elevator_Status)

    def __init__(self, elevator_position : float, position_delta_threshold : float = 0.1):
        self.__elevator_control_msg = Elevator_Control()
        self.__elevator_control_msg.elevator_position = elevator_position
        self.__position_delta_threshold = position_delta_threshold

    def start(self):
        self.elevator_subsystem.publish(self.__elevator_control_msg)

    def update(self):
        pass

    def done(self):
        pass

    def isFinished(self) -> bool:
        if self.elevator_subsystem.get() is None:
            rospy.logerr("No status update present from elevator")
            return False

        return within(self.elevator_subsystem.get().elevator_actual_position, self.__elevator_control_msg.elevator_position, self.__position_delta_threshold)