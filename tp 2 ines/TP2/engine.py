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



    @property
    def fuel(self):  # este é um getter
        """Retorna o combustivel do carro."""
        print('Getter: combustivel acedido')
        return self.__fuel

    @fuel.setter
    def fuel(self, fuel):
        """Define o combustivel do carro."""
        self.__fuel = fuel
        print('Setter: combustivel definido')

    @fuel.deleter
    def fuel(self):
        """Coloca combustivel do carro a None."""
        print('Deleter: combustivel apagado')
        self.__fuel = None
        
        

    @property
    def horse_power(self):  # este é um getter
        """Retorna a potência em cavalos do carro."""
        print('Getter: potência em cavalos acedido')
        return self.__horse_power

    @horse_power.setter
    def horse_power(self, horse_power):
        """Define a potência em cavalos do carro."""
        self.__horse_power = horse_power
        print('Setter: potência em cavalos definido')

    @horse_power.deleter
    def horse_power(self):
        """Coloca potência em cavalos do carro a None."""
        print('Deleter: potência em cavalos apagado')
        self.__horse_power = None



    @property
    def torque(self):  # este é um getter
        """Retorna o torque do carro."""
        print('Getter: torque acedido')
        return self.__torque

    @torque.setter
    def torque(self, torque):
        """Define o torque do carro."""
        self.__torque = torque
        print('Setter: torque definido')

    @torque.deleter
    def torque(self):
        """Coloca torque do carro a None."""
        print('Deleter: torque apagado')
        self.__torque = None



    @property
    def displacement(self):  # este é um getter
        """Retorna o deslocamento do carro."""
        print('Getter: deslocamento acedido')
        return self.__displacement

    @displacement.setter
    def displacement(self, displacement):
        """Define o deslocamento do carro."""
        self.__displacement = displacement
        print('Setter: deslocamento definido')

    @displacement.deleter
    def displacement(self):
        """Coloca deslocamento do carro a None."""
        print('Deleter: deslocamento apagado')
        self.__displacement = None



    @property
    def number_cylinders(self):  # este é um getter
        """Retorna o número de cilindros do carro."""
        print('Getter: número de cilindros acedido')
        return self.__number_cylinders

    @number_cylinders.setter
    def number_cylinders(self, number_cylinders):
        """Define o número de cilindrosl do carro."""
        self.__number_cylinders = number_cylinders
        print('Setter: número de cilindros definido')

    @number_cylinders.deleter
    def number_cylinders(self):
        """Coloca número de cilindros do carro a None."""
        print('Deleter: número de cilindros apagado')
        self.__number_cylinders = None
        
        
        
    @property
    def starting_system(self):  # este é um getter
        """Retorna o ínicio do sistema do carro."""
        print('Getter: ínicio do sistema acedido')
        return self.__starting_system

    @starting_system.setter
    def starting_system(self, starting_system):
        """Define o ínicio do sistema do carro."""
        self.__starting_system = starting_system
        print('Setter: ínicio do sistema definido')

    @starting_system.deleter
    def starting_system(self):
        """Coloca ínicio do sistema do carro a None."""
        print('Deleter: ínicio do sistema apagado')
        self.__starting_system = None
        


    @property
    def dry_weight(self):  # este é um getter
        """Retorna o dry weight do carro."""
        print('Getter: dry weight acedido')
        return self.__dry_weight

    @dry_weight.setter
    def dry_weight(self, dry_weight):
        """Define o dry weight do carro."""
        self.__dry_weight = dry_weight
        print('Setter: dry weight definido')

    @dry_weight.deleter
    def dry_weight(self):
        """Coloca dry weight do carro a None."""
        print('Deleter: dry weight apagado')
        self.__dry_weight = None



    @property
    def manufacturer(self):  # este é um getter
        """Retorna o fabricante do carro."""
        print('Getter: fabricante acedido')
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Define o fabricante do carro."""
        self.__manufacturer = manufacturer
        print('Setter: fabricante definido')

    @manufacturer.deleter
    def manufacturer(self):
        """Coloca fabricante do carro a None."""
        print('Deleter: fabricante apagado')
        self.__manufacturer = None
        
 
    def __str__(self):
        return f"Fuel: {self.fuel}, Horse Power: {self.horse_power}, Torque: {self.torque}, Displacement: {self.displacement},  Number Cylinders: {self.number_cylinders}, Starting System: {self.starting_system}, Dry Weight: {self.dry_weight}, Manufacturer: {self.manufacturer}"

if __name__ == "__main__":
    Engine()
