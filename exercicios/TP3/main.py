"""
===============================================================================================

Disciplina: POO
UALG
Criador: André Vieira - a64108
Descrição: Calculadora de vencimentos de membros de uma empresa com diferentes ranks.

===============================================================================================

Classes

    Pessoa - Getter, Setter e Deleter
        nome        - dados
        morada      - dados
        telefone    - dados

        Subclasse de Pessoa: - Getter, Setter e Deleter
            Fornecedor
                valor_credito - crédito máximo admitido pelo fornecedor
                valor_divida - montante em divida para o fornecedor

            Método em Fornecedor
                obter_saldo = valor_credito - valor_divida

        Subclasse de Pessoa: - Getter, Setter e Deleter
            Empregado
                codigo_setor - dados
                salario_base - dados, vencimento base
                imposto      - valor dado quando e feita a conta

            Metodo em Empregado:
                calcular_salario = salario_base * imposto

            Subclasse de Empregrado: - Getter, setter e deleter
                Administrador
                    ajuda_de_custo - valor 
                    calcular_salario_admin = (salario_base + ajuda_de_custo) * imposto - valor nao classe

            Subclasse de Empregado: Getter, setter e deleter
                Operario
                    valor_producao - quanto $$$ produz o operario
                    valor_comissão - percentagem
                    comissao = valor_producao * valor_comissao

                    calcular_salario_operario = (salario_base + comissao) * imposto

===============================================================================================

    Implemente e faça o override ao método __str__() em cada uma das classes. 

===============================================================================================
    """

import pickle

from pessoa import Pessoa
from fornecedor import Fornecedor
from empregado import Empregado
from administrador import Administrador
from operario import Operario


list_of_pessoa = []
list_of_fornecedor = []
list_of_empreagado = []
list_of_operario = []
list_of_adminstrador = []


def main():
    list_of_pessoa = []
    list_of_fornecedor = []
    list_of_empreagado = []
    list_of_operario = []
    list_of_adminstrador = []

    while True:
        print("========================================================================")
        print("|                                MENU                                  |")
        print("========================================================================")
        print("|                                                                      |")
        print("|        P1 - Nova Pessoa                    P2 - Lista de Pessoas     |")
        print("|                                                                      |")
        print("|        F1 - Novo Fornecedor                F2 - Lista de Fornecedores|")
        print("|                                                                      |")
        print("|        E1 - Nova Empregado                 E2 - Lista de Empregados  |")
        print("|                                                                      |")
        print("|        O1 - Novo Operario                  O2 - Lista de Operarios   |")
        print("|                                                                      |")
        print("|        A1 - Novo Administrador             A2 - Lista de Admins      |")
        print("|                                                                      |")
        print("========================================================================")
        print("|                                                                      |")
        print("|        S - Guardar Listas                  L - Carregar Lista        |")
        print("|                                                                      |")
        print("========================================================================")

        op = input("Opção? ").lower()

        match op:
            case "p1":
                nome = input("Introduzir Nome: ")
                morada = input("Introduzir Morada: ")
                telefone = input("Introduzir Telefone: ")

                new_pessoa = Pessoa(nome, morada, telefone)
                list_of_pessoa.append(new_pessoa)
                print("Nova Pessoa Adicionada!")

            case "p2":
                print_list(list_of_pessoa)


            case "f1":
                valor_credito = input("Introduzir Valor de Crédito: ")
                valor_divida = input("Introduzir Valor de Divida: ")
                
                new_fornecedor = Fornecedor(valor_credito, valor_divida)
                list_of_fornecedor.append(new_fornecedor)
                print("Novo Fornecedor Adicionado!")

            case "f2":
                print_list(list_of_fornecedor)


            case "e1":
                codigo_setor = input("Introduzir Codigo de Setor: ")
                salario_base = input("Introduzir Salario Base:")
                imposto = input("Introduzir Imposto (0 - 1): ")
                
                new_empregado = Empregado(codigo_setor, salario_base, imposto)
                list_of_empregado.append(new_empregado)
                print("Novo Empregado Adiicionado!")
                
            case "e2":
                print_list(list_of_empreagado)


def new_car():
    person_id = ask_id("Person id? ", list_of_persons)
    color_id = ask_id("What is the Color? ", list_of_colors)
    engine_id = ask_id("Engine id? ", list_of_engines)

    brand = input("Enter the car brand: ")
    model = input("Enter the car model: ")
    consumption = input("Enter the fuel consumption (km/l): ")
    kms = input("Enter the current kilometers on the car: ")
    
    new_car = Car(
        owner=list_of_persons[person_id],
        color=list_of_colors[color_id],
        engine=list_of_engines[engine_id],
        brand=brand,
        model=model,
        consumption=consumption,
        kms=kms,
    )

    list_of_cars.append(new_car)
    print("New car added!")


if __name__ == "__main__":
    main()