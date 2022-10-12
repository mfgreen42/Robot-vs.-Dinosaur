
from weapon import Weapon

class Robot:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Slasher', 35)

    def attack(self, dinosaur):
        dinosaur = dinosaur - self.active_weapon.attack_power
        print()
        print(f'{self.name} attacked Trooper for {self.active_weapon.attack_power} damage!')
        print(f'Trooper has {dinosaur} health remaining!')
