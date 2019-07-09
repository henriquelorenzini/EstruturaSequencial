#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Qual sua altura em metros? '))

pesoIdeal = (72.2 * altura) - 58

print ('Com base na sua altura {:.2f}, seu peso ideal é : {:.2f} kg'.format(altura,pesoIdeal))