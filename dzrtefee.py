import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 10)
        self.energy = random.randint(0, 10)

    def is_hungry(self):
        return self.hunger > 5

    def is_tired(self):
        return self.energy < 5

    def play(self):
        if self.is_tired():
            print(f"{self.name} doesnt want to play he is tired")
            self.energy += 2
        else:
            print(f"{self.name} plays and has fun")
            self.energy -= 3
            self.hunger += 1

    def feed(self):
        if self.is_hungry():
            print(f"{self.name} hungry and eats food ")
            self.hunger -= 4
        else:
            print(f"{self.name} doesnt want to eat he is full")

    def sleep(self):
        print(f"{self.name} going to sleep")
        self.energy += 6

    def __str__(self):
        return f"{self.name} - Cat\nHunger: {self.hunger}\nEnergy: {self.energy}"


if __name__ == "__main__":
    cat = Cat("Moritz")

    print("cat's condition:")
    print(cat)
    cat.play()
    cat.feed()
    cat.sleep()
    print(cat)
