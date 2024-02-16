# ========================================================================
# UALG - POO 
# Aluno - 64108
# Exercicio - 9
# ========================================================================

# Implemente as classes apresentadas no diagrama UML da Figura 1.

#   Utilize o Visual Studio Code ou outro IDE avançado.

#   Este diagrama foi escrito segundo as convenções do UML, por isso são necessárias algumas adaptações para a implementação em Python:

#       Os nomes de atributos e métodos devem ser escritos no formato PEP8 – ou seja – em minúsculas, com as palavras separadas por _ (e.g., print_owner()).

#       Os getters e setters dos atributos devem ser implementados como properties, através de decoradores (em vez de funções get e set).

#           Quando se usam properties para encapsular atributos de classes, estes devem ser declarados como privados, ou seja, com um prefixo __ (e.g., self.__forename).

#   Crie um programa que permita, de modo interativo: listar, inserir, remover, e editar carros de uma lista (veja o exemplo em baixo).

#       Crie também uma opção para gravar essa lista num ficheiro (e.g., veja o módulo pickle).


# ========================================================================

# MAIN

# Tem de se mudar as variaveis
# printOwner() --> print_owner() 

# Tudo o que for "get" out "set" vão ser implementadas a partir de decoradores

# propriedades têm de ser privadas em com __nome


from car import Car
from person import Person
from color import Color
from engine import Engine
import pickle

list_of_persons = []
list_of_engines = []
list_of_colors = []
list_of_cars = []


def main():
    while True:
        print("========================================================================")
        print("|                                MENU                                  |")
        print("========================================================================")
        print("|                                                                      |")
        print("|        P1 - New Person                     P2 - List Persons         |")
        print("|                                                                      |")
        print("|        E1 - New Engine                     E2 - List Engines         |")
        print("|                                                                      |")
        print("|        C1 - New Color                      C2 - List Colors          |")
        print("|                                                                      |")
        print("|        V1 - New Car                        V2 - List Cars            |")
        print("|                                                                      |")
        print("========================================================================")
        print("|                                                                      |")
        print("|        S - Save lists                      L - Load lists            |")
        print("|                                                                      |")
        print("========================================================================")

        op = input("Opção? ").lower()

        match op:
            case "p1":
                # TODO: inputs
                new_person = Person()
                list_of_persons.append(new_person)

            case "p2":
                print_list(list_of_persons)

            case "e1":
                # TODO: inputs
                new_engine = Engine()
                list_of_engines.append(new_engine)

            case "e2":
                print_list(list_of_engines)

            case "c1":
                new_color = Color()
                list_of_colors.append(new_color)

            case "c2":
                print_list(list_of_colors)

            case "v1":
                # TODO: inputs
                new_vehicle()

            case "v2":
                print_list(list_of_cars)

            case "s":
                with open("colors_list.pkl", "wb") as f:
                    pickle.dump(list_of_colors, f)

            case "l":
                with open("colors_list.pkl", "rb") as f:
                    list_of_colors = pickle.load(f)
                print_list(list_of_colors)


def print_list(list_of):
    # TODO: improve listing
    print(list(enumerate(list_of)))


def ask_id(msg, input_list):
    # TODO: validate returned id
    print_list(input_list)

    return int(input(msg))


def new_vehicle():
    person_id = ask_id("Person id? ", list_of_persons)
    color_id = ask_id("What is the Color? ", list_of_colors)
    engine_id = ask_id("Engine id? ", list_of_engines)

    new_car = Car(
        owner=list_of_persons[person_id],
        color=list_of_colors[color_id],
        engine=list_of_engines[engine_id],
        brand="???",  # TODO
        model="???",  # TODO
        consumption=-1,  # TODO
        kms=-1,  # TODO
    )

    list_of_cars.append(new_car)


# Only runs if this file is executed directly
if __name__ == "__main__":
    main()
