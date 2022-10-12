

class Dinosaur:


    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power #int
        self.health = 100


    def attack(self, robot):
        robot = robot - self.attack_power
        print()
        print(f'{self.name} attacked Tin Man for {self.attack_power} damage!')
        print(f'Tin Man has {robot} health remaining!')
