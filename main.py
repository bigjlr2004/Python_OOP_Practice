from glasscase_animals import Salamander, Spider, Rat_Snake, Turtle, Copperhead
from petting_animals import Llama, Donkey, Monkey, Teddy_Bear, Koala
from pond_animals import Geese, Goldfish, Catfish, Mallard, Frog


def main():
    George = Goldfish("George", "Albino")
    Kermit = Frog("Kermit", "Green Frog")
    Donkee = Donkey("Donkey", "Talking Donkey", "Evening")
    Drama = Llama("Drama", "House Llama", "Morning")

    print("--Animals--")
    print("------------")
    print(Donkee.name)
    print("------------")
    print(Kermit.name)
    print("------------")
    print(George.name)
    print("------------")
    Drama.print_petter()


if __name__ == "__main__":
    main()
