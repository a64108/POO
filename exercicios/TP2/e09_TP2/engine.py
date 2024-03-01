#!/usr/bin/env python3
"""
@date Feb 15 2024
@authors: pcardoso, j-a-martins
"""


class Engine:
    # TODO: see UML
    def __init__(self, fuel, horse_power, torque, displacement, number_cylinders, starting_system, dry_weight, manufacturer):
        
        self.fuel = fuel
        self.horse_power = horse_power
        self.torque = torque
        self.displacement = displacement
        self.number_cylinders = number_cylinders
        self.starting_system = starting_system
        self.dry_weight = dry_weight
        self.manufacturer = manufacturer


# Only runs if this file is executed directly
if __name__ == "__main__":
    # Test the class
    v8 = Engine()

    print(v8)
