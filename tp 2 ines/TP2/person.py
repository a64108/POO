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
        


    @property
    def forename(self):  # este é um getter
        """Retorna o nome da pessoa."""
        print('Getter: nome acedido')
        return self.__forename

    @forename.setter
    def forename(self, forename):
        """Define o nome da pessoa."""
        self.__forename = forename
        print('Setter: nome definido')

    @forename.deleter
    def forename(self):
        """Coloca nome da pessoa a None."""
        print('Deleter: nome apagado')
        self.__forename = None
        
        
        
    @property
    def surname(self):  # este é um getter
        """Retorna o sobrenome da pessoa."""
        print('Getter: nome acedido')
        return self.__forename

    @surname.setter
    def surname(self, surname):
        """Define o sobrenome da pessoa."""
        self.__surname = surname
        print('Setter: sobrenome definido')

    @surname.deleter
    def surname(self):
        """Coloca sobrenome da pessoa a None."""
        print('Deleter: sobrenome apagado')
        self.__surname = None        
        
        
        
    @property
    def address(self):  # este é um getter
        """Retorna a morada da pessoa."""
        print('Getter: morada acedida')
        return self.__address

    @address.setter
    def address(self, address):
        """Define a  morada da pessoa."""
        self.__address = address
        print('Setter: morada definida')

    @address.deleter
    def address(self):
        """Coloca a morada da pessoa a None."""
        print('Deleter: morada apagada')
        self.__address = None  
        
        
        
    @property
    def cc(self):  # este é um getter
        """Retorna o cartão de crédito da pessoa."""
        print('Getter: cartão de crédito acedido')
        return self.__cc

    @cc.setter
    def cc(self, cc):
        """Define o cartão de crédito da pessoa."""
        self.__cc = cc
        print('Setter: cartão de crédito definido')

    @cc.deleter
    def cc(self):
        """Coloca o cartão de crédito da pessoa a None."""
        print('Deleter: cartão de crédito apagado')
        self.__cc = None        
        


    @property
    def phone(self):  # este é um getter
        """Retorna o número telémovel da pessoa."""
        print('Getter: número telémovel acedido')
        return self.__phone

    @phone.setter
    def phone(self, phone):
        """Define o número telémovel da pessoa."""
        self.__phone = phone
        print('Setter: número telémovel definido')

    @phone.deleter
    def phone(self):
        """Coloca o número telémovel da pessoa a None."""
        print('Deleter: número telémovel apagado')
        self.__phone = None         
    
  
def __str__(self): 
    return f"Forename: {self.forename}, Surname: {self.surname}, Address: {self.address}, Credit Card: {self.cc}, Phone Number: {self.phone_number}" 
  

