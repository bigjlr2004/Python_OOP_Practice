# import the python datetime module to help create a timestamp

from datetime import date


class Llama:

    def __init__(self, name, species):
        # Establish the properties of each animal with a default value.
        self.name = name
        self.species = species
        self.date_added = date.today()


miss_fuzz = Llama("Miss Fuzz", "domestic_llama")

# miss_fuzz.name = "Miss Fuzz"
# miss_fuzz.species = "domestic llama"

print(miss_fuzz.name)
print(miss_fuzz.species)


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


class Copperhead:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = ""
        self.slithering = True


class Rat_Snake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = ""
        self.slithering = True


class Spider:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.crawling = True


class Turtle:
    def __init_(self, name, species):
        self.name = name
        self.species = species
        self.date_added = ""
        self.crawling = ""


class Salamander:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = ""
        self.crawling = True


class Mallard:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Geese:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Goldfish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Catfish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Frog:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


kermit = Frog("Kermit", "green frog")

billy = Catfish("Catfish Billy", "Flathead")

print(billy.name)
print(billy.species)


print(kermit.date_added)
print(kermit.swimming)
print(kermit.name)
