#!/usr/bin/env python3
"""
@date Feb 15 2024
@authors: pcardoso, j-a-martins
"""

from car import Car
from person import Person
from color import Color
from engine import Engine
import pickle

list_of_persons = []
list_of_engines = []
list_of_colors = []
list_of_cars = []


def main():
    while True:
        print("Menu")
        print("P1 - New Person")
        print("P2 - List Persons")

        print("E1 - New Engine")
        print("E2 - List Engines")

        print("C1 - New Color")
        print("C2 - List Colors")

        print("V1 - New Car")
        print("V2 - List Cars")

        print("S - Save lists")
        print("L - Load lists")

        op = input("Op? ").lower()

        match op:
            case "p1":
                # TODO: inputs
                new_person = Person()
                list_of_persons.append(new_person)

            case "p2":
                print_list(list_of_persons)

            case "e1":
                # TODO: inputs
                new_engine = Engine()
                list_of_engines.append(new_engine)

            case "e2":
                print_list(list_of_engines)

            case "c1":
                new_color = Color()
                list_of_colors.append(new_color)

            case "c2":
                print_list(list_of_colors)

            case "v1":
                # TODO: inputs
                new_vehicle()

            case "v2":
                print_list(list_of_cars)

            case "s":
                with open("colors_list.pkl", "wb") as f:
                    pickle.dump(list_of_colors, f)

            case "l":
                with open("colors_list.pkl", "rb") as f:
                    list_of_colors = pickle.load(f)
                print_list(list_of_colors)


def print_list(list_of):
    # TODO: improve listing
    print(list(enumerate(list_of)))


def ask_id(msg, input_list):
    # TODO: validate returned id
    print_list(input_list)

    return int(input(msg))


def new_vehicle():
    person_id = ask_id("Person id? ", list_of_persons)
    color_id = ask_id("What is the Color? ", list_of_colors)
    engine_id = ask_id("Engine id? ", list_of_engines)

    new_car = Car(
        owner=list_of_persons[person_id],
        color=list_of_colors[color_id],
        engine=list_of_engines[engine_id],
        brand="???",  # TODO
        model="???",  # TODO
        consumption=-1,  # TODO
        kms=-1,  # TODO
    )

    list_of_cars.append(new_car)


# Only runs if this file is executed directly
if __name__ == "__main__":
    main()
