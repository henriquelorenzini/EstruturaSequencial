#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius
farenheit = float(input('Quantos graus Farenheit está hoje? '))

celsius = (5*(farenheit - 32)/9)

print ('A temperatura {} °F, em celsius é {:.1f} °C'.format(farenheit, celsius))