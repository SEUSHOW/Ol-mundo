v = float(input('Digite o valor da compra'))
mp = int(input('Escolha o método de pagamento\n[ 1 ] à vista 10% de desconto\n[ 2 ] à vista no cartão 5% de desconto\n'
         '[ 3 ] Parcelado 2x\n[ 4 ] Parcelado 3x ou mais com 20% de jurus\n '))
av = v-(v*10)/100
avc = v-(v*5)/100
p2 = v/2
p3 = v+(v*20)/100


if mp == 1:
      print('Voce pagará à vista {}'.format(av))
elif mp == 2:
    print(' Você pagará à vista{}'.format(avc))
elif mp == 3:
    print('Voce pagará {}'.format(p2))
elif mp == 4:
    vp = int(input('Diga o numero de parcelas '))
    pv = p3 / vp
    print('Voce irá pagar {}'.format(pv))
else:
    v = 0
    print(' tente novamente')


