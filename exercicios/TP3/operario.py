from empregado import Empregado
from pessoa import Pessoa

class Operario(Empregado):
    def __init__ (self, valor_producao, valor_comissao, pessoa, empregado):
        super().__init__(pessoa.nome, pessoa.morada, pessoa.telefone, empregado.codigo_setor, empregado.salario_base, empregado.imposto)

        self.valor_producao = valor_producao                        ### PERGUNTAR PORQUE E FAZER ADMINISTRADOR
        self.valor_comissao = valor_comissao
        self.salario_operario = self.calcular_salario_operario()

    def calcular_salario_operario(self):
        salario_operario = empregado.salario_base + self.valor_comissao - (empregado.salario_base * empregado.imposto)
        salario_operario = format(salario_operario, '.2f')
        return salario_operario

    # Getter, setter, e deleter de valor_producao
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

    # Getter, setter e deleter de valor_comissao
    @property
    def valor_comissao(self):
        """Retorna o valor de comissao do Operario."""
        print('Getter: Valor de Comissao Acedido')
        return self.__valor_comissao

    @valor_comissao.setter
    def valor_comissao(self, valor_comissao):
        """Define o valor de comissao do operario."""
        self.__valor_comissao = valor_comissao
        print('Setter: Valor de Comissao do Operario Definido')

    @valor_comissao.deleter
    def valor_comissao(self):
        """Coloca o Valor de Comissao do Operario a None."""
        print('Deleter: Valor de Comissao Apagado')
        self.__valor_comissao = None

    def __str__(self): 
        return f"Valor de Producao: {self.valor_producao}, Valor de Comissao: {self.valor_comissao}, Salário Operário: {self.calcular_salario_operario()}" 
  
if __name__ == "__main__":

    pessoa = Pessoa("Zé Dias", "Rua 123 ABC", "987654321")
    empregado = Empregado("113", 1000, 0.2, pessoa)
    operario = Operario(100, 0.1, pessoa, empregado)
    print(f"Operário: {operario}")
