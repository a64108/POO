#!/usr/bin/env python3
"""
@date Feb 15 2024
@authors: pcardoso, j-a-martins
"""


class Person:
    # TODO: see UML
    def __init__(self, forename, surname, address, cc, phone):
        
        self.forename = forename
        self.surname = surname
        self.address = address
        self.cc = cc
        self.phone = phone
        

    # Get Person Info
    def get_forename(self):
        return self.forename
    
    def get_surname(self):
        return self.surname
    
    def get_address(self):
        return self.address
    
    def get_cc(self):
        return self.cc
    
    def get_phone(self):
        return self.phone
    
    # Set Person Info

    def set_forename(self,d):
        self.forename = d

    def set_surname(self,d):
        self.surname = d

    def set_address(self,d):
        self.address = d
    
    def set_cc(self,d):
        self.cc = d
    
    def set_phone(self, d):
        self.phone = d

# New person
        d = (input('Insert Forename:'))
        person.set_forename

        d = (input('Insert Surname:'))
        person.set_surname

        d = (input('Insert Adress:'))
        person.set_address

        d = (input('Insert CC:'))
        person.set_cc

        d = (input('Insert Phone Number:'))
        person.set_phone 

# Read person

        print('Person Forename:', person.get_forename())
        print('Person Surname:', person.get_surname())
        print('Person Adress:', person.get_address())
        print('Person CC: ', person.get_cc())
        print('Person Phone Number:', person.get_phone())

# Only runs if this file is executed directly
if __name__ == "__main__":
    # Test the class
    ze = Person()

    print(ze)
