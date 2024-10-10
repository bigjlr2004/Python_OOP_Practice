from glasscase_animals import Salamander, Spider, Rat_Snake, Turtle, Copperhead
from petting_animals import Llama, Donkey, Monkey, Teddy_Bear, Koala
from pond_animals import Geese, Goldfish, Catfish, Mallard, Frog
from attractions import SnakePit, Wetlands, PettingZoo


def main():
    George = Goldfish("George", "Albino")
    Kermit = Frog("Kermit", "Green Frog")
    varmint_village = PettingZoo("Varmint Village")
    Donkee = Donkey("Donkey", "Talking Donkey", "Evening", "Samwhiches")
    Drama = Llama("Drama", "House Llama", "Morning", "Fruit Loops")
    varmint_village.habitate(Donkee)
    varmint_village.habitate(Drama)

    for animal in varmint_village.animals:
        print(
            f"You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}"
        )

    print("--Animals--")
    print("------------")
    print(Donkee.name)
    print("------------")
    print(Kermit.name)
    print("------------")
    print(George.name)
    print("------------")
    Drama.feed()
    print(Donkee)


if __name__ == "__main__":
    main()
