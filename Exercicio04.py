# Faça um Programa que peça as 4 notas bimestrais e mostre a média

# entrada
nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))
nota_4 = float(input('Digite a quarta nota: '))

# processamento
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# saída
print('A média das notas é: {:.2f}'.format(media))
