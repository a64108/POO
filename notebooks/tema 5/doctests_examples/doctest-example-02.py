"""
Exemplo de uso do doctest.

O modulo fornece a função converte_temperatura().
"""


def converte_temperatura(temp_inicial, unidade_origem, unidade_destino):
    """
    Converte e devolve a temperatura da unidade de_unidade para para_unidade (2 casas de decimais de precisão).

    :param temp_inicial: temperatura inicial
    :param da_unidade: unidade de entrada (elemento de 'K', 'F', 'C')
    :param para_unidade: unidade de saída (elemento de 'K', 'F', 'C')
    :return: valor da temperatura na unidade de saida

    >>> converte_temperatura(273.16, 'K', 'C')
    0.01

    >>> converte_temperatura(-40, 'C', 'F')
    -40.0

    >>> converte_temperatura(450, 'F', 'K')
    505.37222

    >>> converte_temperatura(450, 'f', 'K')
    Traceback (most recent call last):
    ...
    AssertionError: Unidade de temperatura nao conhecida: f

    >>> converte_temperatura(-450, 'C', 'K')
    Traceback (most recent call last):
    ...
    AssertionError: Temperatura inválida: -450 C é inferior a 0 K (zero absoluto)

    >>> converte_temperatura("450", 'f', 'K')
    Traceback (most recent call last):
    ...
    AssertionError: O primeiro argumento deve ser um número

    """

    # Dicionário com as funções de conversão das diferentes unidades para K (Kelvin)
    kelvin_destino = {
        "K": lambda k: k,
        "C": lambda k: k + 273.15,
        "F": lambda k: (k + 459.67) * 5 / 9,
    }

    # Dicionário com a conversão de K para as diferentes unidades
    kelvin_origem = {
        "K": lambda k: k,
        "C": lambda k: k - 273.15,
        "F": lambda k: k * 9 / 5 - 459.67,
    }

    assert isinstance(
        temp_inicial, (int, float)
    ), "O primeiro argumento deve ser um número"

    assert (
        unidade_origem in kelvin_origem
    ), f"Unidade de temperatura nao conhecida: {unidade_origem}"

    assert (
        unidade_destino in kelvin_destino
    ), f"Unidade de temperatura nao conhecida: {unidade_destino}"

    # Verifica se é necessário converter
    if unidade_origem == unidade_destino:
        return temp_inicial

    temp_final = kelvin_destino[unidade_origem](temp_inicial)

    assert (
        temp_final > 0
    ), f"Temperatura inválida: {temp_inicial} {unidade_origem} é inferior a 0 K (zero absoluto)"

    temp_final = round(kelvin_origem[unidade_destino](temp_final), 5)

    return temp_final


if __name__ == "__main__":
    import doctest

    failure_count, test_count = doctest.testmod(verbose=True)
    # Terminar o programa se houver falhas nos doctests
    if failure_count > 0:
        exit()

    print(50 * "-")

    # E se quisermos testar a função com outros valores?
    casos_teste = [
        ((273.16, "K"), (0.010000000000047748, "C")),
        ((-40, "C"), (-40, "F")),
        ((450, "F"), (505.3722222222222, "K")),
        (("450", "F"), (505.3722222222222, "K")),
    ]

    for caso in casos_teste:
        # Desempacotar os valores de cada caso de teste
        (temp_orig, unidade_orig), (temp_dest, unidade_dest) = caso
        
        # Testar as conversões de temperatura
        try:
            temp = converte_temperatura(temp_orig, unidade_orig, unidade_dest)
            print(f"{temp_orig} {unidade_orig} = {temp} {unidade_dest}")

            # Verificar se o resultado está correto (com uma margem de erro de 1x10^-7)
            if abs(temp - temp_dest) > 1e-7:
                print(f"[ERRO: {temp} != {temp_dest}]\nO teste falhou!")
                exit()
        except AssertionError as e:
            print(e)

    # Haverá outras formas menos confusas de testar a função converte_temperatura()?
    # Sim! Podemos usar o módulo unittest ou o pytest.
