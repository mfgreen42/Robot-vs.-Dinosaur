
from robot import Robot
from dinosaur import Dinosaur


class Battlefield:

    def __init__(self):
        self.robot = Robot('Tin Man',)
        self.dinosaur = Dinosaur('Trooper', 20)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        
        
    def display_welcome(self):
        print("""
Welcome to the Battlefield! 
Only one will be victorious 
        
        """)


    def battle_phase(self):
        battle_bool = True
        while battle_bool == True:
            self.dinosaur.attack(self.robot.health)
            self.robot.health = self.robot.health - self.dinosaur.attack_power
            if self.robot.health > 0:
                battle_bool = True
            else:
                battle_bool = False
            self.robot.attack(self.dinosaur.health)
            self.dinosaur.health = self.dinosaur.health - self.robot.active_weapon.attack_power
            if self.dinosaur.health > 0:
                battle_bool = True
            else:
                battle_bool = False

    def display_winner(self):
        pass




