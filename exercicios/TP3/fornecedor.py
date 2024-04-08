from pessoa import Pessoa  # Assuming 'pessoa' is the file name containing the Pessoa class definition

class Fornecedor(Pessoa):
    def __init__(self, valor_credito, valor_divida, pessoa):
        super().__init__(pessoa.nome, pessoa.morada, pessoa.telefone)
        self.valor_credito = valor_credito
        self.valor_divida = valor_divida
        self.valor_fornecedor = self.valor_fornecedor()

    def valor_fornecedor(self):
        return self.valor_credito - self.valor_divida
    
    # Getter, setter, e deleter de valor_credito
    @property
    def valor_credito(self):
        """Retorna o Valor de Credito do Fornecedor."""
        print('Getter: Valor Credito Acedido')
        return self.__valor_credito

    @valor_credito.setter
    def valor_credito(self, valor_credito):
        """Define o Valor de Credito do Fornecedor."""
        self.__valor_credito = valor_credito
        print('Setter: Valor de Credito do Fornecedor Definido')

    @valor_credito.deleter
    def valor_credito(self):
        """Define o Valor de Credito do Fornecedor a None."""
        print('Deleter: Valor Credito do Fornecedor Apagado')
        self.__valor_credito = None

    # Getter, setter, e deleter de valor_divida
    @property
    def valor_divida(self):
        """Retorna o Valor de Divida do Fornecedor."""
        print('Getter: Valor Divida Acedido')
        return self.__valor_divida

    @valor_divida.setter
    def valor_divida(self, valor_divida):
        """Define o Valor de Divida do Fornecedor."""
        self.__valor_divida = valor_divida
        print('Setter: Valor de Divida do Fornecedor Definido')

    @valor_divida.deleter
    def valor_divida(self):
        """Coloca o Valor de Divido do Fornecedor a None."""
        print('Deleter: Valor Divida do Fornecedor Apagado')
        self.__valor_divida = None

    def __str__(self): 
        return f"Valor de Crédito: {self.valor_credito}, Valor de Divida: {self.valor_divida}, Valor do Fornecedor: {self.valor_fornecedor}" 
  
  
if __name__ == "__main__":
   
    pessoa = Pessoa("Zé Dias", "Rua 123 ABC", "987654321")
    fornecedor = Fornecedor(1000, 250, pessoa)
    print(f"Fornecedor: {fornecedor}")
