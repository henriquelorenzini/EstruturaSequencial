#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit

celsius = float(input('Quantos graus celsius está hoje? '))

farenheit = (celsius * 9)/5 + 32

print ('A temperatura {} °C, em farenheit é {:.1f} °F'.format(celsius, farenheit))