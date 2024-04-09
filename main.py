import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.min_attack_power = 0
        self.max_attack_power = 20
    def attack(self, other):
        attack_power = random.randint(self.min_attack_power, self.max_attack_power)
        other.health -= attack_power
        print(f"{self.name} атакует {other.name} и наносит {attack_power} урона.")
    def is_alive(self):
        return self.health > 0
class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")
    def start(self):
        print("Игра начинается!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} умер. {self.player.name} победил!")
                break
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")

            # Ход компьютера
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} умер. {self.computer.name} победил!")
                break
            print(f"У {self.player.name} осталось {self.player.health} здоровья.")

game = Game("Bloodseeker")
game.start()