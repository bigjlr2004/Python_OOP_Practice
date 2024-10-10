from datetime import date


class Llama:

    def __init__(self, name, species, shift):
        # Establish the properties of each animal with a default value.
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True

    def print_petter(self):
        print(
            f"{self.name} the {self.species} is available to pet during the {self.shift} shift."
        )


class Donkey:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True


class Goat:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True


class Teddy_Bear:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True


class Monkey:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True


class Koala:
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True
