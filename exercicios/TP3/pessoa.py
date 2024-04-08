"""
classe pessoa
"""

class Pessoa():
    def __init__ (self, nome, morada, telefone):

        self.nome = nome
        self.morada = morada
        self.telefone = telefone


# Getter, setter e deleter de nome

    @property
    def nome(self):
        """Retorna o nome da Pessoa."""
        print('Getter: Nome Acedido')
        return self.__nome

    @nome.setter
    def nome(self, nome):
        """Define o nome da Pessoa."""
        self.__nome = nome
        print('Setter: Nome da Pessoa Definido')

    @nome.deleter
    def nome(self):
        """Coloca Nome da Pessoa a None."""
        print('Deleter: Nome da Pessoa Apagado')
        self.__nome = None

# Getter, setter e deleter de morada

    @property
    def morada(self):
        """Retorna a morada da Pessoa."""
        print('Getter: Morada Acedida')
        return self.__morada

    @morada.setter
    def morada(self, morada):
        """Define o nome da Morada."""
        self.__morada = morada
        print('Setter: Morada da Pessoa Definido')

    @morada.deleter
    def morada(self):
        """Coloca Morada da Pessoa a None."""
        print('Deleter: Morada da Pessoa Apagado')
        self.__morada = None

# Getter, setter e deleter de telefone

    @property
    def telefone(self):
        """Retorna o telefone da Pessoa."""
        print('Getter: Telefone Acedido')
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        """Define o telefone da Pessoa."""
        self.__telefone = telefone
        print('Setter: Telefone da Pessoa Definido')

    @telefone.deleter
    def telefone(self):
        """Coloca telefone da Pessoa a None."""
        print('Deleter: Telefone da Pessoa Apagado')
        self.__telefone = None

  
    def __str__(self): 
        return f"Nome: {self.nome}, Morada: {self.morada}, Telefone: {self.telefone}" 
  
if __name__ == "__main__":

    pessoa = Pessoa("Zé Dias", "Rua 123 ABC", "987654321")
    print(f"Pessoa: {pessoa}")
