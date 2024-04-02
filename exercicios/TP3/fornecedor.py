
from pessoa import Pessoa

class Fornecedor(Pessoa):
    def __init__ (self, valor_credito, valor_divida):

        self.valor_credito = valor_credito
        self.valor_divida = valor_divida


# Getter, setter e deleter de valor de credito

    @property
    def valor_credito(self):
        """Retorna o valor de credito da Pessoa."""
        print('Getter: Valor Credito Acedido')
        return self.__valor_credito

    @valor_credito.setter
    def valor_credito(self, valor_credito):
        """Define o valor de credito da Pessoa."""
        self.__valor_credito = valor_credito
        print('Setter: Valor de Credito da Pessoa Definido')

    @valor_credito.deleter
    def valor_credito(self):
        """Coloca Valor de Credito da Pessoa a None."""
        print('Deleter: Nome da Pessoa Apagado')
        self.__valor_credito = None

# Getter, setter e deleter de valor de divida

    @property
    def valor_divida(self):
        """Retorna o valor de divida da Pessoa."""
        print('Getter: Valor Divida Acedido')
        return self.__valor_divida

    @valor_divida.setter
    def valor_divida(self, valor_divida):
        """Define o valor de divida da Pessoa."""
        self.__valor_divida = valor_divida
        print('Setter: Valor de Divida da Pessoa Definido')

    @valor_divida.deleter
    def valor_divida(self):
        """Coloca Valor de Divida da Pessoa a None."""
        print('Deleter: Divida da Pessoa Apagado')
        self.__valor_divida = None


    def __str__(self): 
        return f"Valor de Crédito: {self.valor_credito}, Valor de Divida: {self.valor_divida}" 
  
if __name__ == "__main__":
    Fornecedor(Pessoa)