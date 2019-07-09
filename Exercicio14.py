#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input('Qual sua altura em metros? '))

pesoIdealHomem = (72.2 * altura) - 58
pesoIdealMulher = (62.1*altura) - 44.7

print ('Com base na sua altura {:.2f}, se você for homem, seu peso ideal é : {:.2f} kg'
       ' \nSe você for mulher, seu peso ideal é: {:.2f} kg'.format(altura,pesoIdealHomem,pesoIdealMulher))