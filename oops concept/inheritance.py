class animal:
    alive = True
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(animal):
    pass

class Fish(animal):
    pass

class Hawk(animal):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()