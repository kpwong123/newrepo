class Person:
    def __init__(self, name, age, sex, birth_year):
        self.name = name
        self.age = age
        self.sex = sex
        self.birth_year = birth_year
    def person_function(self):
        if self.sex == "M":
            pronoun = "He"
            sex_display = "male"
        elif self.sex == "F":
            pronoun = "She"
            sex_display = "female"
        else:
            pass
        print(self.name + " is " + str(self.age) + " years old. " + pronoun + " is a " + sex_display + ".")

p1 = Person("Mary", 23, "F", 1997)

p1.age = 24
p1.birth_year = 1996

print(p1.age, p1.birth_year)
p1.person_function()

import random as ran
class CustomList:
  def __init__(self, num):
    self.my_list = [ran.randrange(1,101,1) for _ in range(num)]

obj = CustomList(5)
print(obj)

class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __call__(self):
        print ('Person: {}, Age: {}'.format(self.name, self.age))

person = Person3("John", 23)

person()

class Entity:
    '''Callable to update the entity's position.'''

    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def __call__(self, x, y):
        '''Change the position of the entity.'''
        self.x, self.y = x, y

point = Entity(12, 32, 34)
print(point.x, point.y)
point(12,23)
print(point.x, point.y)