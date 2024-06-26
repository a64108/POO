from pessoa import Pessoa

class Empregado(Pessoa):
    def __init__ (self, codigo_setor, salario_base, imposto, pessoa):
        super().__init__(pessoa.nome, pessoa.morada, pessoa.telefone)

        self.codigo_setor = codigo_setor
        self.salario_base = salario_base
        self.imposto = imposto
        self.salario_empregado = self.calcular_salario_empregado()

    def calcular_salario_empregado(self):
        salario_empregado = self.salario_base - (self.salario_base * self.imposto)
        salario_empregado = format(salario_empregado, '.2f')
        return salario_empregado

# Getter, setter e deleter de codigo do setor

    @property
    def codigo_setor(self):
        """Retorna o codigo do setor do Empregado."""
        print('Getter: Codigo do Setor Acedido')
        return self.__codigo_setor

    @codigo_setor.setter
    def codigo_setor(self, codigo_setor):
        """Define o codigo do setor do Empregado."""
        self.__codigo_setor = codigo_setor
        print('Setter: Codigo do Setor do Empregado Definido')

    @codigo_setor.deleter
    def codgio_setor(self):
        """Coloca o Codigo do Setor do Empregado a None."""
        print('Deleter: Codigo do Setor Apagado')
        self.__codigo_setor = None

# Getter, setter e deleter de valor do salario base

    @property
    def salario_base(self):
        """Retorna o salario base do Empregado."""
        print('Getter: Salario Base Acedido')
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        """Define o Salario Base do Empregado."""
        self.__salario_base = salario_base
        print('Setter: Salario Base do Empregado Definido')

    @salario_base.deleter
    def salario_base(self):
        """Coloca o Salario Base do Empregado a None."""
        print('Deleter: Salario Base Apagado')
        self.__salario_base = None

# Getter, setter e deleter de imposto

    @property
    def imposto(self):
        """Retorna o Imposto do Empregado."""
        print('Getter: Imposto Acedido')
        return self.__imposto

    @imposto.setter
    def imposto(self, imposto):
        """Define o Imposto do Empregado."""
        self.__imposto = imposto
        print('Setter: Imposto do Empregado Definido')

    @imposto.deleter
    def imposto(self):
        """Coloca o Imposto do Empregado a None."""
        print('Deleter: Imposto Apagado')
        self.__imposto = None


    def __str__(self): 
        return f"Codigo do Setor: {self.codigo_setor}, Salario Base: {self.salario_base}, Imposto: {self.imposto}, Salário Empregado: {self.calcular_salario_empregado()}"
  
if __name__ == "__main__":

    pessoa = Pessoa("Zé Dias", "Rua 123 ABC", "987654321")
    empregado = Empregado("113", 1000, 0.2, pessoa)
    print(f"Empregado: {empregado}")