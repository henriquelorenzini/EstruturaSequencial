#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
print ('Cada litro de tinta pinta uma área de 3 metros quadrados')
metros = float(input('Quantos metros você deseja pintar ? '))

precoLata = 80.0
capacidadeLata = 18

litros = metros/3
latas = litros / capacidadeLata
precoTotal = latas * precoLata

print ('Sera necessário um total de {:.0f} latas'.format(latas))
print ('O preço total foi de R${:.2f}'.format(precoTotal))
