#!/usr/bin/env python3
"""
@date Feb 15 2024
@authors: pcardoso, j-a-martins
"""


class Color:
    def __init__(self, color_name, r=0, g=0, b=0):
        self.color_name = color_name
        self.r = r
        self.g = g
        self.b = b
        
        
# Getter e setter abaixo (como fazer o owner)

    @property
    def color_name(self):  # este é um getter
        """Retorna o nome da cor."""
        print('Getter: cor acedida')
        return self.__color_name

    @color_name.setter
    def color_name(self, color_name):
        """Define o nome da cor"""
        self.__color_name = color_name
        print('Setter: cor definida')

    @color_name.deleter
    def color_name(self): 
        """Coloca o nome da cor a None."""
        print('Deleter: cor apagada')
        self.__color_name = None


    @property
    def rgb(self):  # este é um getter
        """Retorna o valor RGB."""
        return self.__r, self.__g, self.__b
  
  
    @rgb.setter
    def rgb(self, rgb):
        """Define o valor RGB"""
        r, g, b = rgb
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            self.__r = r
            self.__g = g
            self.__b = b
        else:
            raise ValueError("Os valores de R, G, B devem estar entre 0 e 255")


    @rgb.deleter
    def rgb(self): 
        """Coloca o valor da cor a None."""
        print('Deleter: valor apagado')
        self.__r = self.__g = self.__b = None

    def __str__(self):
        return f"Color Name: {self.color_name}, Valor RGB: ({self.r}, {self.g}, {self.b})"

if __name__ == "__main__":
    Color()