#!/usr/bin/env python3
"""
@date Feb 15 2024
@authors: pcardoso, j-a-martins
"""


class Color:
    # TODO: see UML
    def __init__(self, color_name, RGB):
        
        self.color_name = color_name
        self.RGB = RGB


# Only runs if this file is executed directly
if __name__ == "__main__":
    # Test the class
    red = Color()

    print(red)
