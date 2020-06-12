data = int(input('Digite a seu ano de nascimento: '))
atual = int(input('Digite o ano atual: '))
idade = atual-data
mirim = idade <= 9
infantil = 9 < idade <= 14
junior = 14 < idade <= 19
senior = 19 < idade <= 25
master = 25 > idade

if mirim:
     print('voce entrará na modalidade: Mirim')
elif infantil:
     print('Voce entrará para a modalidade: Infantil')
elif junior:
     print('Voce entrará na modalidade: Junior')
elif senior:
     print('Voce entrará para a modalidade: Senior')
else:
     print('Voce entrará para a modalidade: master')


