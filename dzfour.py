import random

class Student:
    def __init__(self, name):
        self.name = name
        self.money = 1000
        self.energy = 100
        self.knowledge = 50
        self.health = 100
        self.year = 1

    def work(self):
        earnings = random.randint(100, 300)
        print(f"{self.name} works and earns money {earnings} euro")
        self.money += earnings

    def study(self):
        knowledge_gain = random.randint(10, 30)
        print(f"{self.name} studies and receives {knowledge_gain} knowledge")
        self.knowledge += knowledge_gain
        self.money -= 100

    def rest(self):
        energy_gain = random.randint(10, 30)
        print(f"{self.name} rests and restores{energy_gain} energy")
        self.energy += energy_gain
        self.money -= 50

    def find_job(self):
        if self.knowledge >= 70 and self.money < 500:
            print(f"{self.name} found a job")
            self.money += 500
        else:
            print(f"{self.name} looking for a job but hasn't received any offers yet")

    def year_passed(self):
        self.year += 1
        self.health -= random.randint(5, 15)
        self.energy -= random.randint(10, 20)

    def is_successful(self):
        return self.knowledge >= 150 and self.money >= 1000 and self.health >= 50

    def live_one_year(self):
        while self.year <= 12:
            print(f"\nГод {self.year}:")
            self.work()
            self.study()
            self.find_job()
            self.rest()
            self.year_passed()
            print(f"{self.name} have {self.knowledge} knowledge, {self.money} euro, {self.energy} energy, and {self.health} health")
            if self.is_successful():
                print(f"{self.name} Successfully completed the training and achieved my goals")
                break
        else:
            print(f"{self.name} was unable to complete his studies in a year")

if __name__ == "__main__":
    student = Student("Moritz")
    student.live_one_year()