#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
lado = float(input('defina um valor para o lado do quadrado: '))

area = lado * lado

dobroArea = 2 * area

print ('O lado do quadrado é: ' + str(lado))
print ('A area do quadrado é: ' + str(area))
print ('O dobro da area do quadrado é: ' + str(dobroArea))