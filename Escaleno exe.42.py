c1 = float(input('digite a primeira medida de seu triangulo'))
c2 = float(input('digite a segunda medida : '))
c3 = float(input('Digite a uarta medida do triangulo:'))

if  c1 + c2 > c3 and c2 + c3 > c2 and c3 + c1 > c2:
    print('pode ser formado um triângulo')

    if c1 == c2 == c3:
     print('O seu triangulo é Euilátero')
    elif c1 != c2 != c3 != c1:
     print('o triangulo é escaleno')
    else:
     print('O triangulo é isosceles')
else:
 print('Nao pode formar triangulo')
