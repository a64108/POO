#!/usr/bin/env python3
"""
@date Feb 15 2024
@authors: pcardoso, j-a-martins
"""

from person import Person
from color import Color
from engine import Engine


class Car:
    def __init__(self, owner, color, engine, brand, model, consumption, kms):
        # Verify the argument types
        assert isinstance(owner, Person)
        assert isinstance(color, Color)
        assert isinstance(engine, Engine)

        # Define the properties
        self.brand = brand
        self.model = model
        self.consumption = consumption
        self.kms = kms

        # TODO: "encapsulate" + addkms + ... see UML


# Only runs if this file is executed directly
if __name__ == "__main__":
    # Test the class
    ze = Person()
    v8 = Engine()
    red = Color()

    car = Car(
        owner=ze,
        color=red,
        engine=v8,
        brand="UMM",
        model="Alter",
        consumption=8,
        kms=100000,
    )

    print(car)
