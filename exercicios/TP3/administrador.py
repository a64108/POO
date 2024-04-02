from empregado import Empregado

class Administrador(Empregado):
    def __init__ (self, ajuda_de_custo):
        
            self.ajuda_de_custo = ajuda_de_custo


# Getter, setter e deleter de codigo do setor

    @property
    def ajuda_de_custo(self):
        """Retorna o valor da ajuda de custo do Adminstrador."""
        print('Getter: Ajuda de Custo Acedido')
        return self.__ajuda_de_custo

    @ajuda_de_custo.setter
    def ajuda_de_custo(self, ajuda_de_custo):
        """Define a ajuda de custo do Administrador."""
        self.__ajuda_de_custo = ajuda_de_custo
        print('Setter: Ajuda de Custo de Adminstrador Definido')

    @ajuda_de_custo.deleter
    def ajuda_de_custo(self):
        """Coloca a ajuda de custo do Adminstrador a None."""
        print('Deleter: Ajuda de Custo Apagado')
        self.__ajuda_de_custo = None



    def __str__(self): 
        return f"Ajuda de Custo: {self.ajuda_de_custo}" 
  
if __name__ == "__main__":
    Administrador(Empregado)
