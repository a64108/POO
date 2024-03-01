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
        print("========================================================================")
        print("|                                MENU                                  |")
        print("========================================================================")
        print("|                                                                      |")
        print("|        P1 - Nova Pessoa                    P2 - Lista de Pessoas     |")
        print("|                                                                      |")
        print("|        E1 - Novo Motor                     E2 - Lista de Motores     |")
        print("|                                                                      |")
        print("|        C1 - Nova Cor                       C2 - Lista de Cores       |")
        print("|                                                                      |")
        print("|        V1 - Nova Viatura                   V2 - Lista de Viaturas    |")
        print("|                                                                      |")
        print("========================================================================")
        print("|                                                                      |")
        print("|        S - Guardar Listas                  L - Carregar Lista        |")
        print("|                                                                      |")
        print("========================================================================")

        op = input("Opção? ").lower()

        match op:
            case "p1":
                # TODO: inputs
                forename = input("Enter forename: ")
                surname = input("Enter surname: ")
                address = input("Enter address: ")
                cc = input("Enter credit card number: ")
                phone = input("Enter phone number: ")

                new_person = Person(forename, surname, address, cc, phone)
                list_of_persons.append(new_person)
                print("New person added!")

            case "p2":
                print_list(list_of_persons)


            case "e1":
                # TODO: inputs
                fuel = input("Enter fuel: ")
                horse_power = float(input("Enter horse power: "))
                torque = input("Enter torque: ")
                displacement = input("Enter displacement: ")
                number_cylinders = float(input("Enter number cylinders: "))
                starting_system = input("Enter starting system: ")
                dry_weight = input("Enter dry weight: ")
                manufacturer = input("Enter manufacturer: ")
                
                new_engine = Engine(fuel, horse_power, torque, displacement, number_cylinders, starting_system, dry_weight, manufacturer)
                list_of_engines.append(new_engine)
                print("New engine added!")

            case "e2":
                print_list(list_of_engines)


            case "c1":
                
                color_name = input("Enter color: ")
                RGB = input("Enter color RGB: ")
                
                new_color = Color(color_name, RGB)
                list_of_colors.append(new_color)  # noqa: F823
                print("New color added!")

            case "c2":
                print_list(list_of_colors)


            case "v1":
                # TODO: inputs
                owner = input("Enter owner: ")
                color = input("Enter color: ")
                engine = input("Enter engine: ")
                brand = input("Enter brand: ")
                model = input("Enter model: ")
                consumption = float(input("Enter consumption: "))
                kms = float(input("Enter kms: "))
                
                new_car = Car(owner, color, engine, brand, model, consumption, kms)
                list_of_cars.append(new_car)
                print("New car added!")

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


def new_car():
    person_id = ask_id("Person id? ", list_of_persons)
    color_id = ask_id("What is the Color? ", list_of_colors)
    engine_id = ask_id("Engine id? ", list_of_engines)

    brand = input("Enter the car brand: ")
    model = input("Enter the car model: ")
    consumption = float(input("Enter the fuel consumption (km/l): "))
    kms = float(input("Enter the current kilometers on the car: "))
    
    new_car = Car(
        owner=list_of_persons[person_id],
        color=list_of_colors[color_id],
        engine=list_of_engines[engine_id],
        brand=brand,
        model=model,
        consumption=consumption,
        kms=kms,
    )

    list_of_cars.append(new_car)
    print("New car added!")

# Only runs if this file is executed directly
if __name__ == "__main__":
    main()
