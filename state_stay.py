import motor as MotorControl
import random
from sensordetection import sensordetect
from stateMachine import *
from listPicker import RandomList

class state_wander():
    def __init__(self, stateMachine):
        self._stateMachine = stateMachine
        # put your commands here
        self.commands = [
        [MotorControl.forward, .2, .4],
        [MotorControl.backward, .1, .2],
        [MotorControl.wait, 2, 3],
        [MotorControl.turnLeft, .2, .5],
        [MotorControl.turnRight, .2, .5]
        ]
        self.commandChances = [
        25,
        2,
        60,
        10,
        10
        ]
    def Act(self):
        # gets a random command
        command = RandomList(self.commands, self.commandChances)
        # runs the script inside the commands array and gives it random times
        command[0](random.uniform(command[1],command[2]))

    def Reason(self):
        # stops application if the distance of the sensor is lower then the value given
        if sensordetect() < 10:
            print("stopping cus of distance")
            exit()
