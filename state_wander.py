import motor as MotorControl
import random
from stateMachine import *

class state_wander():
    def __init__(self, stateMachine):
        self._stateMachine = stateMachine
        # put your commands here
        self.commands = [
        [MotorControl.forward, .2, .5] * 1,
        [MotorControl.backward, .1, .3] * 1,
        [MotorControl.wait, 2, 3.5] * 6,
        [MotorControl.turnLeft, .1, .5] * 1,
        [MotorControl.turnRight, .1, .5] * 1
        ]
    def Act(self):
        # gets random int for a command from the commands array
        commandNumber = random.randint(0, 9)
        print(commandNumber)
        print(self.commands)
        # makes it a simple to use variable
        command = random.choice(self.commands)
        # runs the script inside the commands array and gives it random times
        command[0](random.uniform(command[1],command[2]))
        print(command)

    def Reason(self):
        # little somthing so you won't get an infinite loop
        if random.randint(0, 100) < 30:
            exit()
