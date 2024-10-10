class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

    def habitate(self, animal):
        self.animals.append(animal)


class SnakePit:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "slimy, slinky, creepy critters to scare you"
        self.animals = list()


class Wetlands:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "swimming, diving, gliding critters that like it wet "
        self.animals = list()
