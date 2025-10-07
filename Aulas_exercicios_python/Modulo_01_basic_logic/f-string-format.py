# f-string
nome = 'Stwarty'
print(f'Meu nome é {nome}') 
idade = 33
altura = 1.75
print(f'Meu nome é {nome} ,tenho {idade} anos e '\
'minha altura é {altura}') 
# formatação de strings com metodo format
print('Meu nome é {0} ,tenho {1} anos e ' \
'minha altura é {2:.3f}'.format(nome, idade, altura))
# {:.3f} -> 3 casas decimais
print('Meu nome é {1} ,tenho {0} anos e ' \
'minha altura é {2:.2f}'.format(nome, idade, altura))
# utilizando indices na ordem que quiser, 
# atenção com os indices repetidos ou tipo de dado
print('Meu nome é {n} ,tenho {i} anos e ' \
'minha altura é {a:.1f}'.format(n=nome, i=idade, a=altura))
# utilizando parametros nomeados
print('Meu nome é {n} ,tenho {i} anos e ' \
'minha altura é {a:.0f}'.format(n=nome, i=idade, a=altura))
# {:.0f} -> 0 casas decimais
