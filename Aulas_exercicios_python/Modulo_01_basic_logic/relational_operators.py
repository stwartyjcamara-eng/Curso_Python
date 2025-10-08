# Operadores relacinais
# >, <, >=, <=, ==, !=
# > maior que
# < menor que
# >= maior ou igual a
# <= menor ou igual a
# == igual a
# != diferente de

input_idade = int(input('Qual sua idade? '))
if input_idade < 18:
    print('Você é menor de idade')
elif input_idade >= 18 and input_idade < 65:
    print('Você é adulto')
elif input_idade >= 65:
    print('Você é idoso')
