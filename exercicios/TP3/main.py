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


            case "c1":
                color_name = input("Enter color: ")
                
                r = int(input("Enter red component (0-255): "))
                g = int(input("Enter green component (0-255): "))
                b = int(input("Enter blue component (0-255): "))
               
                if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                    new_color = Color(color_name, r, g, b)  
                    list_of_colors.append(new_color)  
                    print("New color added!")

            case "c2":
                print_list(list_of_colors)


            case "v1":
                owner = input("Enter owner: ")
                color = input("Enter color: ")
                engine = input("Enter engine: ")
                brand = input("Enter brand: ")
                model = input("Enter model: ")
                consumption = input("Enter consumption: ")
                kms = input("Enter kms: ")
                
                new_car = Car(owner, color, engine, brand, model, consumption, kms)
                list_of_cars.append(new_car)
                print("New car added!")

            case "v2":
                print_list(list_of_cars)

            case "s":
                with open("persons_list.pkl", "wb") as f:
                    pickle.dump(list_of_persons, f)
                    
                with open("engines_list.pkl", "wb") as f:
                    pickle.dump(list_of_engines, f)
                    
                with open("colors_list.pkl", "wb") as f:
                    pickle.dump(list_of_colors, f)
                    
                with open("cars_list.pkl", "wb") as f:
                    pickle.dump(list_of_cars, f)                   
                    
                    
            case "l":
                with open("persons_list.pkl", "rb") as f:
                    list_of_persons = pickle.load(f)
                print_list(list_of_persons)
                
                with open("engines_list.pkl", "rb") as f:
                    list_of_engines = pickle.load(f)
                print_list(list_of_engines)
                
                with open("colors_list.pkl", "rb") as f:
                    list_of_colors = pickle.load(f)
                print_list(list_of_colors)
                
                with open("cars_list.pkl", "rb") as f:
                    list_of_cars = pickle.load(f)
                print_list(list_of_cars)                


def print_list(list_of):
    for idx, item in enumerate(list_of):
        print(f"{idx}: {item}")


def ask_id(msg, input_list):
    print_list(input_list)
    return int(input(msg))


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