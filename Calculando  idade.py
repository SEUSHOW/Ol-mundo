i = int(input('Diga a sua idade em numero : '))
nascimento = 2020-i
alistamento = 18

if i == 18:
    print('Pelas contas voce nasceu em {}, e este ano você será obrigado a comparecer na junta militar'.format(nascimento))
elif alistamento < i :
    print('Hà {} anos voce compareceu na junta militar?'.format(i-alistamento))
else:
    print('Ainda faltam {} anos para voce se alistar '.format(alistamento-i))
