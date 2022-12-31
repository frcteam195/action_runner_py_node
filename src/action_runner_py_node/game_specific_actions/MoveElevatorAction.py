from default_actions.Action import Action
from ck_ros_msgs_node.msg import Elevator_Control, Elevator_Status
import rospy
from frc_robot_utilities_py_node.BufferedROSMsgHandlerPy import BufferedROSMsgHandlerPy
from ck_utilities_py_node.ckmath import *

class MoveElevatorAction(Action):
    elevator_publisher = rospy.Publisher(name='ElevatorControl', data_class=Elevator_Control, queue_size=50, tcp_nodelay=True)
    elevator_status = BufferedROSMsgHandlerPy(Elevator_Status)

    def __init__(self, elevator_position : float, position_delta_threshold : float = 0.1):
        self.__elevator_control_msg = Elevator_Control()
        self.__elevator_control_msg.elevator_position = elevator_position
        self.__position_delta_threshold = position_delta_threshold
        self.elevator_status.register_for_updates("ElevatorStatus")

    def start(self):
        self.elevator_publisher.publish(self.__elevator_control_msg)

    def update(self):
        pass

    def done(self):
        pass

    def isFinished(self) -> bool:
        return within(self.elevator_status.get().elevator_actual_position, self.__elevator_control_msg.elevator_position, self.__position_delta_threshold)