peso = float(input('Didgite seu peso '))
altura = float(input('Digite sua altura '))

imc = peso/(altura**2)
if imc <= 16 :
    print('Voce está desnutrido com massa corpórea de {:.2f}'.format(imc))
elif imc <= 17:
    print('magreza moderada com massa corpórea de {:.2f}'.format(imc))
elif imc <= 18.5:
    print('magreza leve com massa corpóral de {:.2f}'.format(imc))
elif imc <= 25:
    print('Saudável com massa corporal de {:.2f}'.format(imc))
elif imc <= 30:
    print('Voce está com sobre peso com massa corporal de {:.2f}'.format(imc))
elif imc <= 35:
    print('obesidade nível 1 com massa corporal de {:.2f}'.format(imc))
elif imc <= 40:
    print('Obesidade nível 2 (severa) com massa corporal de {:.2f}'.format(imc))
else:
    print('Voce esta com obesidade grau 3 (mórbida) com massa corporal de {:.2f}'.format(imc))