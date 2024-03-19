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

        # Define as propriedades
        self.owner = owner
        self.color = color
        self.engine = engine
        self.brand = brand
        self.model = model
        self.consumption = consumption
        self.kms = kms

# Getter ,setter e deleter de owner
    
    @property
    def owner(self):
        """Retorna o dono do carro."""
        print('Getter: dono acedida')
        return self.__owner

    @owner.setter
    def owner(self, owner):
        """Define o dono do carro."""
        self.__owner = owner
        print('Setter: Dono definida')

    @owner.deleter
    def owner(self):
        """Coloca dono do carro a None."""
        print('Deleter: dono apagado')
        self.__cor = None
        

# Getter ,setter e deleter de color
                
    @property
    def color(self):
        """Retorna a cor do carro."""
        print('Getter: cor acedida')
        return self.__cor

    @color.setter
    def color(self, color):
        """Define a cor do carro."""
        self.__color = color
        print('Setter: cor definida')

    @color.deleter
    def color(self): 
        """Coloca cor do carro a None."""
        print('Deleter: cor apagada')
        self.__color = None
    
# Getter ,setter e deleter de engine
            
    @property
    def engine(self):  # este é um getter
        """Retorna o motor do carro."""
        print('Getter: motor acedido')
        return self.__engine

    @engine.setter
    def engine(self, engine):
        """Define o motor do carro."""
        self.__engine = engine
        print('Setter: motor definido')

    @engine.deleter
    def engine(self):  
        """Coloca o motor do carro a None."""
        print('Deleter: motor apagado')
        self.__engine = None
    
# Getter ,setter e deleter de marca    

    @property
    def brand(self):
        """Retorna a marca do carro."""
        print('Getter: marca acedida')
        return self.__brand

    @brand.setter
    def brand(self, brand):
        """Define o marca do carro."""
        self.__brand = brand
        print('Setter: marca definida')

    @brand.deleter
    def brand(self): 
        """Coloca o marca do carro a None."""
        print('Deleter: marca apagada')
        self.__brand = None
    
    # Getter ,setter e deleter de modelo

    @property
    def model(self):
        """Retorna o modelo do carro."""
        print('Getter: modelo acedido')
        return self.__model

    @model.setter
    def model(self, model):
        """Define o modelo do carro."""
        self.__model = model
        print('Setter: modelo definido')

    @model.deleter
    def model(self):  
        """Coloca o modelo do carro a None."""
        print('Deleter: modelo apagado')
        self.__model = None    
    
# Getter ,setter e deleter de consumo

    @property
    def consumption(self):
        """Retorna o consumo do carro."""
        print('Getter: consumo acedido')
        return self.__consumption

    @consumption.setter
    def consumption(self, consumption):
        """Define o consumo do carro."""
        self.__consumption = consumption
        print('Setter: consumo definido')

    @consumption.deleter
    def consumption(self):  
        """Coloca o consumo do carro a None."""
        print('Deleter: consumo apagado')
        self.__consumption = None 

    # Getter ,setter e deleter de kms 
           
    @property
    def kms(self):
        """Retorna os kms do carro."""
        print('Getter: kms acedidos')
        return self.__ckms

    @kms.setter
    def kms(self, kms):
        """Define os kms do carro."""
        self.__kms = kms
        print('Setter: kms definidos')

    @kms.deleter
    def kms(self):  
        """Coloca o consumo do carro a None."""
        print('Deleter: kms apagados')
        self.__kms = None 
        

def __str__(self):
    return f"Owner: {self.owner} Color: {self.color}, Engine: {self.engine}, Brand: {self.brand}, Model: {self.model}, Consumption: {self.consumption}, Kms: {self.kms}"

