
from robot import Robot
from dinosaur import Dinosaur


class Battlefield:

    def __init__(self):
        self.robot = Robot
        self.dinosaur = Dinosaur

    def run_game(self):
        self.display_welcome()
    


    def display_welcome(self):
        print("""
Welcome to the Battlefield! 
Only one will be victorious 
        
        """)


    def battle_phase(self):
        pass


    def display_winner(self):
        pass




