#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#A - o produto do dobro do primeiro com metade do segundo .
#B - a soma do triplo do primeiro com o terceiro.
#C- o terceiro elevado ao cubo.

num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
num3 = float(input('Digite o terceiro valor: '))

a = (num1 * 2) * (num2 / 2)
b = (num1 * 3) + num3
c = (num3 * num3 * num3)

print('Os valores declarados foram: {:.1f}, {:.1f}, {:.1f}'.format(num1,num2,num3))
print('A - o produto do dobro do primeiro com metade do segundo: ' +str(a))
print('B - a soma do triplo do primeiro com o terceiro: ' + str(b))
print('C- o terceiro elevado ao cubo: ' + str(c))
