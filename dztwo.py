import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 10)
        self.energy = random.randint(0, 10)

    def is_hungry(self):
        print("Cat is hungry")
        return self.hunger > 5

    def to_sleep(self):
        print("I will sleep")
        self.energy += 6

    def is_tired(self):
        print("Cat is tired")
        return self.energy < 5

    def play(self):
        if self.is_tired():
            print(f"{self.name} doesn't want to play, he is tired.")
            self.energy += 2
        else:
            print(f"{self.name} plays and has fun!")
            self.energy -= 3
            self.hunger += 1

    def feed(self):
        if self.is_hungry():
            print(f"{self.name} hungry and eats food with appetite")
            self.hunger -= 4
        else:
            print(f"{self.name} doesn't want to eat, he's full")

    def __str__(self):
        return f"{self.name} - Cat\nHungry: {self.hunger}\nEnergy: {self.energy}"

    