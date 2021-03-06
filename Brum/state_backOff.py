import motor as MotorControl
from stateMachine import *
from sensordetection import sensordetect


class state_backOff():
    def __init__(self, stateMachine):
        self._stateMachine = stateMachine
        self.isDone = False
    def Act(self):
        MotorControl.turnLeft(.1)
        if sensordetect() > 30:
            self.isDone = True
    def Reason(self):
        if self.isDone is True:
            self.isDone = False
            self._stateMachine.SetState("stay")
