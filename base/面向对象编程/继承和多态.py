class Animal(object):
    def run(self):
        print('animal is runing')


class Dog(Animal):
    def run(self):
        print('dog is runing')

class Cat(Animal):
    def run(self):
        print('cat is runing')

a = Animal()
b = Dog()
c = Cat()
print(isinstance(b,Dog))
print(isinstance(b,Animal))

def run_twice(animal):
    animal.run()

run_twice(b)