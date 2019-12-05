# Dog Class file
from task_animal_class import *

# Creating Dog class:
class Dog(Animal):
    # Define inheritance attributes from Animal class and specific Dog class attributes
    def __init__(self, owner, name, id, collar):
        # Use supper.__init__ to keep selected arguments as default from Animal
        super().__init__()
        self.owner = owner
        self.name = name
        self.id_number = id
        self.dog_collar = collar

    # Define polymorphism methods from Animal class
    def make_sound(self): # Polymorphism here. Altering make_sound returns from Animal class method
        return 'WOOF ~ Stranger!! ~'

    # Define Dog class specific methods
    def eat_bone(self):
        return 'AHUMM!! Crunchy!!'

    def run(self):
        return 'HAAA!! ~ Exahusted ~'

    def greet_owner(self):
        return 'WOOF!! ~ Greeting ~'

