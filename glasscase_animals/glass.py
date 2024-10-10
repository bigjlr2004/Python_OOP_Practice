from datetime import date


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
