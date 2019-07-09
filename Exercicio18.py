#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

print('Cada litro de tinta pinta uma área de 6 metros quadrados e é vendida em latas de 18 litros que custam R$ 80,00 e/ou galões de 3,6 litros que custam R$ 25,00\n\n')
area = float(input('Qual o tamanho da área a ser pintada em m²? '))

litros = (area/6.0) *1.1 #10% de folga
latas = int(litros/18)
galoes = int(litros/3.6)

if (litros % 18 != 0):
    latas += 1
    precoLata = latas * 80.00
# Calculo de galoes
if (litros % 3.6 != 0):
    galoes += 1
    precoGaloes = galoes * 25.00

# Calculo misturando latas e galoes
mixLatas = int(litros / 18.0)
mixGaloes = int((litros - (mixLatas * 18.0)) / 3.6)
if ((litros - (mixLatas * 18.0) % 3.6 != 0)):
    mixGaloes += 1
    precoLataGalao = (mixLatas * 80.00) + (mixGaloes * 25.00)

print ('A quantidade de latas vai ser de {:.0f} e o valor vai ser de R$ {:.2f}'.format(latas,precoLata))
print ('A quantidade de galões vai ser de {:.0f} e o valor vai ser de R$ {:.2f}'.format(galoes,precoGaloes))
print ('A quantidade de latas vai ser de {:.0f} e a de galoes vai ser de {:.0f}, o valor total ficou R$ {:.2f}'.format(mixLatas,mixGaloes,precoLataGalao))