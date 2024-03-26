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
        
        self.owner = owner
        self.color = color
        self.engine = engine
        self.brand = brand
        self.model = model
        self.consumption = consumption
        self.kms = kms

# Getter, setter e deleter de owner
    
    @property
    def owner(self):
        """Retorna o dono do carro."""
        print('Getter: Owner Acedido')
        return self.__owner

    @owner.setter
    def owner(self, owner):
        """Define o owner do veiculo."""
        self.__owner = owner
        print('Setter: Owner Definido')

    @owner.deleter
    def owner(self):
        """Coloca Owner do veiculo a None."""
        print('Deleter: Owner Apagado')
        self.__color = None
        

# Getter, setter e deleter de color
                
    @property
    def color(self):
        """Retorna a cor do veiculo."""
        print('Getter: Color Acedida')
        return self.__color

    @color.setter
    def color(self, color):
        """Define a cor do veiculo."""
        self.__color = color
        print('Setter: Color Definida')

    @color.deleter
    def color(self): 
        """Coloca cor do carro a None."""
        print('Deleter: color Apagada')
        self.__color = None
    

# Getter, setter e deleter de engine

    @property
    def engine(self):
        """Retorna o modelo motor do veiculo."""
        print('Getter: Motor Acedido')
        return self.__engine

    @engine.setter
    def engine(self, engine):
        """Define o modelo do motor do carro."""
        self.__engine = engine
        print('Setter: Motor Definido')

    @engine.deleter
    def engine(self):  
        """Coloca o motor do carro a None."""
        print('Deleter: Motor Apagado')
        self.__engine = None
    

# Getter, setter e deleter de brand

    @property
    def brand(self):
        """Retorna a marca do veiculo."""
        print('Getter: Brand Acedida')
        return self.__brand

    @brand.setter
    def brand(self, brand):
        """Define o brand do veiculo."""
        self.__brand = brand
        print('Setter: Brand Definida')

    @brand.deleter
    def brand(self): 
        """Coloca o marca do carro a None."""
        print('Deleter: Brand Apagada')
        self.__brand = None
    

# Getter, setter e deleter de model

    @property
    def model(self):
        """Retorna o modelo do carro."""
        print('Getter: Model Acedido')
        return self.__model

    @model.setter
    def model(self, model):
        """Define o modelo do veiculo."""
        self.__model = model
        print('Setter: Modelo Definido')

    @model.deleter
    def model(self):  
        """Coloca o modelo do carro a None."""
        print('Deleter: Modelo Apagado')
        self.__model = None    
    

# Getter, setter e deleter de consumption

    @property
    def consumption(self):
        """Retorna o consumo do veiculo."""
        print('Getter: Consumo Acedido')
        return self.__consumption

    @consumption.setter
    def consumption(self, consumption):
        """Define o consumo do carro."""
        self.__consumption = consumption
        print('Setter: Consumo Definido')

    @consumption.deleter
    def consumption(self):  
        """Coloca o consumo do veiculo a None."""
        print('Deleter: Consumo Apagado')
        self.__consumption = None 
        

# Getter, setter e deleter de kms

    @property
    def kms(self):
        """Retorna os kms do veiculo."""
        print('Getter: KMs Acedidos')
        return self.__kms

    @kms.setter
    def kms(self, kms):
        """Define os kms do veiculo."""
        self.__kms = kms
        print('Setter: KMs Definidos')

    @kms.deleter
    def kms(self):  
        """Coloca o consumo do veiculo a None."""
        print('Deleter: KMs Apagados')
        self.__kms = None 
        

    def __str__(self):
        return f"Owner: {self.owner} Color: {self.color}, Engine: {self.engine}, Brand: {self.brand}, Model: {self.model}, Consumption: {self.consumption}, Kms: {self.kms}"


if __name__ == "__main__":
    Car()
