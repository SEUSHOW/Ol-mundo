print('Olá mundo!')
n = int(input('Digite um número para transforma-lo '))
print('Agora escolha:\n[ 1 ]  para BINÁRIO.\n[ 2 ] pata Octal\n[ 3 ]Apara HEXADECIMÁL')
r = int(input('Pode escolher a base de transformação do número {}: '.format(n)))

if r == 1:
    print('O número {} convertido para Binário é {}'.format(n,bin(n)[2:]))
elif r == 2:
    print('O numero {} convertido para  Octal é {}'.format(n,oct(n)[2:]))
elif r == 3 :
    print('O número {} convertido para Héxadecimal é {}'.format(n,hex(n)[2]))
else:
    print('Esse numero não está cadastrado tente denovo')











