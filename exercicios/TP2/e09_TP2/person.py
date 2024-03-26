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
        

# Getter, setter e deleter de forename

    @property
    def forename(self):
        """Retorna o nome da pessoa."""
        print('Getter: Nome Acedido')
        return self.__forename

    @forename.setter
    def forename(self, forename):
        """Define o nome da pessoa."""
        self.__forename = forename
        print('Setter: Nome Definido')

    @forename.deleter
    def forename(self):
        """Coloca nome da pessoa a None."""
        print('Deleter: Nome Apagado')
        self.__forename = None
        


# Getter, setter e deleter de surname
        
    @property
    def surname(self):
        """Retorna o sobrenome da pessoa."""
        print('Getter: Sobrenome Acedido')
        return self.__surname

    @surname.setter
    def surname(self, surname):
        """Define o sobrenome da pessoa."""
        self.__surname = surname
        print('Setter: Sobrenome Definido')

    @surname.deleter
    def surname(self):
        """Coloca sobrenome da pessoa a None."""
        print('Deleter: Sobrenome Apagado')
        self.__surname = None        
        
        

# Getter, setter e deleter de address

    @property
    def address(self):
        """Retorna a morada."""
        print('Getter: Morada Acedida')
        return self.__address

    @address.setter
    def address(self, address):
        """Define a Morada."""
        self.__address = address
        print('Setter: Morada Definida')

    @address.deleter
    def address(self):
        """Coloca a morada da pessoa a None."""
        print('Deleter: Morada Apagada')
        self.__address = None  
        
        

# Getter, setter e deleter de credit card

    @property
    def cc(self):
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
        


# Getter, setter e deleter de phone number

    @property
    def phone(self):
        """Retorna o número telémovel da pessoa."""
        print('Getter: Número Telefone Acedido')
        return self.__phone

    @phone.setter
    def phone(self, phone):
        """Define o número telefone."""
        self.__phone = phone
        print('Setter: Número Telefone Definido')

    @phone.deleter
    def phone(self):
        """Coloca o número telefone a None."""
        print('Deleter: Número telefone Apagado')
        self.__phone = None         
    
  
    def __str__(self): 
        return f"Forename: {self.forename}, Surname: {self.surname}, Address: {self.address}, Credit Card: {self.cc}, Phone Number: {self.phone}" 
  
if __name__ == "__main__":
    Person()
