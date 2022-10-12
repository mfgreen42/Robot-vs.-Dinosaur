from robot import Robot

class Dinosaur:


    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power #int
        self.health = 100


    def attack(self, robot):
        robot -= robot
        print('Dinosaur attacked Robot for xx damage!')
        print('Robot has xx health remaining!')
