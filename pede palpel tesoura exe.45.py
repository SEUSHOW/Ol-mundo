from random import choice
from time import sleep

escolha = int(input('Escolha\n [ 1 ] para pedra\n [ 2 ] para papel\n [ 3 ] para tesoura\n '))
lista = [1, 2, 3]
pc = choice(lista)

print('pedra')
sleep(1)
print('papel')
sleep(1)
print('tesoura')
sleep(1)
print('=-'*11)
if pc == escolha:
    print('empate')
elif escolha == 1 and pc == 2:
    print('Voce perdeu escolhendo pedra contra papel')
elif escolha == 2 and pc == 3:
    print('Voce perdeu escolhendo papel contra tesoura')
elif escolha == 3 and pc == 1:
    print('Voce perdeu escolhendo tesoura contra pedra')
elif escolha == 1 and pc == 3:
    print('Voce ganhou escolhendo pedra contra tesoura')
elif escolha == 2 and pc == 1:
    print('Voce ganhou jogando papel contra pedra')
else:
    escolha == 3 and pc == 2
    print('Voce ganhou escolhendo tesoura contra papel')
print('=-'*11)





