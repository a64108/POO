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
                    calcular_salario_admin = (salario_base + ajuda_de_custo) * imposto

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