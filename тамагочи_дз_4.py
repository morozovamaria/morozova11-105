import time

class Tamagochi:
    def __init__(self,name):
        self.name = name
        self.meal = 100
        self.health = 100

    def damage(self):
        self.health -= 20

    def hunger(self):
        self.meal -= 20
        if self.meal < 0:
            self.meal = 0
            self.damage()

    def feed(self):
        self.meal += 20
        if self.meal > 100:
            self.meal = 100
        if self.health < 100:
            self.heal()

    def heal(self):
        self.health += 20

pet = Tamagochi('Matvei')

current_time = time.time()
while pet.health > 0:
    if int(time.time()-current_time) == 1:
        print('Здоровье:', pet.health)
        print('Голод:', pet.meal)
        answer = input("Покормить? да/нет ")
        if answer == 'да':
            pet.feed()
        elif answer == 'нет':
            pet.hunger()
        current_time = time.time()

print('Matvei died')