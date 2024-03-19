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
    list_of_persons = []
    list_of_engines = []
    list_of_colors = []
    list_of_cars = []
    
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

        op = input("Opção? ").lower()

        match op:
            case "p1":
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
                
                r = int(input("Enter red component (0-255): "))
                g = int(input("Enter green component (0-255): "))
                b = int(input("Enter blue component (0-255): "))
               
                if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                    new_color = Color(color_name, r, g, b)  
                    list_of_colors.append(new_color)  
                    print("New color added!")

            case "c2":
                print_list(list_of_colors)


            case "v1":
                owner = input("Enter owner: ")
                color = input("Enter color: ")
                engine = input("Enter engine: ")
                brand = input("Enter brand: ")
                model = input("Enter model: ")
                consumption = input("Enter consumption: ")
                kms = input("Enter kms: ")
                
                new_car = Car(owner, color, engine, brand, model, consumption, kms)
                list_of_cars.append(new_car)
                print("New car added!")

            case "v2":
                print_list(list_of_cars)

            case "s":
                with open("persons_list.pkl", "wb") as f:
                    pickle.dump(list_of_persons, f)
                    
                with open("engines_list.pkl", "wb") as f:
                    pickle.dump(list_of_engines, f)
                    
                with open("colors_list.pkl", "wb") as f:
                    pickle.dump(list_of_colors, f)
                    
                with open("cars_list.pkl", "wb") as f:
                    pickle.dump(list_of_cars, f)                   
                    
                    
            case "l":
                with open("persons_list.pkl", "rb") as f:
                    list_of_persons = pickle.load(f)
                print_list(list_of_persons)
                
                with open("engines_list.pkl", "rb") as f:
                    list_of_engines = pickle.load(f)
                print_list(list_of_engines)
                
                with open("colors_list.pkl", "rb") as f:
                    list_of_colors = pickle.load(f)
                print_list(list_of_colors)
                
                with open("cars_list.pkl", "rb") as f:
                    list_of_cars = pickle.load(f)
                print_list(list_of_cars)                


def print_list(list_of):
    for idx, item in enumerate(list_of):
        print(f"{idx}: {item}")


def ask_id(msg, input_list):
    print_list(input_list)
    return int(input(msg))


def new_car():
    person_id = ask_id("Person id? ", list_of_persons)
    color_id = ask_id("What is the Color? ", list_of_colors)
    engine_id = ask_id("Engine id? ", list_of_engines)

    brand = input("Enter the car brand: ")
    model = input("Enter the car model: ")
    consumption = input("Enter the fuel consumption (km/l): ")
    kms = input("Enter the current kilometers on the car: ")
    
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
