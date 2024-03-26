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



# Getter, setter e deleter de fuel

    @property
    def fuel(self):
        """Retorna o combustivel do carro."""
        print('Getter: Tipo de Combustivel Acedido')
        return self.__fuel

    @fuel.setter
    def fuel(self, fuel):
        """Define o combustivel do carro."""
        self.__fuel = fuel
        print('Setter: Tipo de Combustivel Definido')

    @fuel.deleter
    def fuel(self):
        """Coloca combustivel do carro a None."""
        print('Deleter: Tipo de Combustivel Apagado')
        self.__fuel = None
        
        

# Getter, setter e deleter de horse power

    @property
    def horse_power(self):
        """Retorna a potência em cavalos do carro."""
        print('Getter: Potência em Cavalos Acedido')
        return self.__horse_power

    @horse_power.setter
    def horse_power(self, horse_power):
        """Define a potência em cavalos do carro."""
        self.__horse_power = horse_power
        print('Setter: Potência em Cavalos Definido')

    @horse_power.deleter
    def horse_power(self):
        """Coloca potência em cavalos do carro a None."""
        print('Deleter: Potência em Cavalos Apagado')
        self.__horse_power = None



# Getter, setter e deleter de torque

    @property
    def torque(self):
        """Retorna o torque do carro."""
        print('Getter: Torque Acedido')
        return self.__torque

    @torque.setter
    def torque(self, torque):
        """Define o torque do carro."""
        self.__torque = torque
        print('Setter: Torque Definido')

    @torque.deleter
    def torque(self):
        """Coloca torque do carro a None."""
        print('Deleter: Torque Apagado')
        self.__torque = None



# Getter, setter e deleter de displacement

    @property
    def displacement(self):
        """Retorna o deslocamento de água do veiculo."""
        print('Getter: Deslocamento de Água Acedido')
        return self.__displacement

    @displacement.setter
    def displacement(self, displacement):
        """Define o deslocamento de água do veiculo."""
        self.__displacement = displacement
        print('Setter: Deslocamento Definido')

    @displacement.deleter
    def displacement(self):
        """Coloca Deslocamento de Água do Veiculo a None."""
        print('Deleter: Deslocamento Apagado')
        self.__displacement = None



# Getter, setter e deleter de number of cylinders

    @property
    def number_cylinders(self):
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
        
        

# Getter, setter e deleter do sistema de arranque

    @property
    def starting_system(self):
        """Retorna o nome do sistema de arranque do carro."""
        print('Getter: Sistema de Arranque Acedido')
        return self.__starting_system

    @starting_system.setter
    def starting_system(self, starting_system):
        """Define o sistema de arranque do carro."""
        self.__starting_system = starting_system
        print('Setter: Sistema de Arranque Definido')

    @starting_system.deleter
    def starting_system(self):
        """Coloca o sistema de arranque do carro a None."""
        print('Deleter: Sistema de Arranque Apagado')
        self.__starting_system = None
        


# Getter, setter e deleter de peso bruto

    @property
    def dry_weight(self):
        """Retorna o dry weight do carro."""
        print('Getter: Dry Weight Acedido')
        return self.__dry_weight

    @dry_weight.setter
    def dry_weight(self, dry_weight):
        """Define o dry weight do carro."""
        self.__dry_weight = dry_weight
        print('Setter: Dry Weight Definido')

    @dry_weight.deleter
    def dry_weight(self):
        """Coloca dry weight do carro a None."""
        print('Deleter: Dry Weight Apagado')
        self.__dry_weight = None



# Getter, setter e deleter do fabricante

    @property
    def manufacturer(self):
        """Retorna o fabricante do carro."""
        print('Getter: fabricante Acedido')
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Define o Fabricante do Carro."""
        self.__manufacturer = manufacturer
        print('Setter: Fabricante Definido')

    @manufacturer.deleter
    def manufacturer(self):
        """Coloca fabricante do carro a None."""
        print('Deleter: Fabricante Apagado')
        self.__manufacturer = None
        
 
    def __str__(self):
        return f"Fuel: {self.fuel}, Horse Power: {self.horse_power}, Torque: {self.torque}, Displacement: {self.displacement},  Number Cylinders: {self.number_cylinders}, Starting System: {self.starting_system}, Dry Weight: {self.dry_weight}, Manufacturer: {self.manufacturer}"

if __name__ == "__main__":
    Engine()
