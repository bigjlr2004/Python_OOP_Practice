from datetime import date


class Llama:

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value.
        self.name = name
        self.species = species
        self.date_added = date.today()


class Donkey:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


class Goat:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


class Teddy_Bear:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


class Monkey:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


class Koala:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
