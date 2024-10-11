from datetime import date

import random
from datetime import datetime


def generate_unique_id():
    now = datetime.now()

    timestamp = now.strftime("%Y%m%d%H%M%S")

    random_number = random.randint(1000, 9999)

    unique_id = f"{timestamp}{random_number}"

    return unique_id


class Animal:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.__chip_number = generate_unique_id()
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species} and chip number {self.__chip_number}"


@property
def chip_number(self):
    return self.__chip_number


@chip_number.setter
def chip_number(self, num):
    pass
