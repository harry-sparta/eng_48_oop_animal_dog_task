# Run file
from task_animal_class import *
from task_dog_class import *

## Creating 2 animals
## Animal class takes 0 argument (self)
animal_1 = Animal()
animal_2 = Animal()
## Executing animal_1 and animal_2 methods
print(animal_1.sleep())
print(animal_2.eat())
print(animal_2.make_sound())


## Creating 2 dogs
## Dog class takes 4 argument (self, owner, name, id, collar)
dog_1 = Dog('Bob', 'Nigel', '007', '101 Brixton')
dog_2 = Dog('Jane', 'Henry', '888', '10 Moorgate')
## Executing dog_1 and dog_2 methods
print(dog_1.eat())
print(dog_1.sleep())
print(dog_1.eat_bone())
print(dog_2.make_sound())
print(dog_2.greet_owner())
print(dog_2.run())