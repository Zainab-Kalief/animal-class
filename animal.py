class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def healthStatus(self):
        print self.health
        return self

wildAnimal = Animal('Goat',50)
wildAnimal.walk().walk().walk().run().run().healthStatus()



class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

dodger = Dog('oni',200)
dodger.walk().walk().walk().run().run().pet().healthStatus()



class Dragon(Animal):
    def __init__(self, name,health):
        super(Dragon, self).__init__(name,health)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def healthStatus(self):
        print 'I am a Dragon' #override the func by changing the action or return
        return self

kalisi = Dragon('GOT',500)
kalisi.healthStatus()



class Bird(Animal):
    def __init__(self, name, health):
        super(Bird, self).__init__(name, health)

angryB = Bird('pop',10)
angryB.healthStatus() #this will refer to parent func
