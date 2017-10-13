#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running....')        


def run_twice(animal):
    animal.run()
    animal.run()


dog = Dog()
dog.run()

cat = Cat()
cat.run()

run_twice(Animal())
run_twice(dog)

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)


print(isinstance('aba', str))

