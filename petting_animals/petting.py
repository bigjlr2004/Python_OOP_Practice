from datetime import date
from Animal import Animal

class Llama(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        # Establish the properties of each animal with a default value.
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

    def print_petter(self):
        print(
            f"{self.name} the {self.species} is available to pet during the {self.shift} shift."
        )

class Donkey(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

    def print_petter(self):
        print(
            f"{self.name} the {self.species} is available to pet during the {self.shift} shift."
        )


class Goat(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
    
    def print_petter(self):
        print(
            f"{self.name} the {self.species} is available to pet during the {self.shift} shift."
        )

    


class Teddy_Bear(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

    def print_petter(self):
        print(
            f"{self.name} the {self.species} is available to pet during the {self.shift} shift."
        )


class Monkey(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

    def print_petter(self):
        print(
            f"{self.name} the {self.species} is available to pet during the {self.shift} shift."
        )


class Koala(Animal):
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, shift, food, chip_num)
        self.shift = shift
        self.walking = True

    def print_petter(self):
        print(
            f"{self.name} the {self.species} is available to pet during the {self.shift} shift."
        )
