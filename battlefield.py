
from robot import Robot
from dinosaur import Dinosaur


class Battlefield:

    def __init__(self):
        self.robot = Robot('Tin Man')
        self.dinosaur = Dinosaur('Trooper', 20)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()


    def display_welcome(self):
        print("""
Welcome to the Battlefield! 
Only one will be victorious 
        
        """)


    def battle_phase(self):
        self.dinosaur.attack(self.robot.health)
        self.robot.attack(self.dinosaur.health)
        

    def display_winner(self):
        pass




