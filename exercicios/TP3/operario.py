from empregado import Empregado

class Operario(Empregado):
    def __init__ (self, valor_producao, valor_comissao, ):
        
            self.valor_producao = valor_producao
            self.valor_comissao = valor_comissao


# Getter, setter e deleter de codigo do setor

    @property
    def valor_producao(self):
        """Retorna o valor de producao do Operario."""
        print('Getter: Valor de Producao Acedido')
        return self.__valor_producao

    @valor_producao.setter
    def valor_producao(self, valor_producao):
        """Define o valor de producao do operario."""
        self.__valor_producao = valor_producao
        print('Setter: Valor de Producao do Operario Definido')

    @valor_producao.deleter
    def valor_producao(self):
        """Coloca o Valor de Producao do Operario a None."""
        print('Deleter: Valor de Producao Apagado')
        self.__valor_producao = None

# Getter, setter e deleter de codigo do setor

    @property
    def valor_comissao(self):
        """Retorna o valor de comissao do Operario."""
        print('Getter: Valor de Comissao Acedido')
        return self.__valor_comissao

    @valor_comissao.setter
    def valor_comissoa(self, valor_comissao):
        """Define o valor de comissoa do operario."""
        self.__valor_comissao = valor_comissao
        print('Setter: Valor de Comissao do Operario Definido')

    @valor_comissao.deleter
    def valor_comissao(self):
        """Coloca o Valor de Comissao do Operario a None."""
        print('Deleter: Valor de Comissao Apagado')
        self.__valor_comissao = None



    def __str__(self): 
        return f"Valor de Producao: {self.valor_producao}, Valor de Comissao: {self.valor_comissao}" 
  
if __name__ == "__main__":
    Operario(Empregado)
