#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario = float(input('Qual é o valor da sua hora de trabalho? '))
horasTrabalhadas = int (input('Quantas horas você trabalhou esse mês? '))

valorAReceber = salario * horasTrabalhadas

print ('Você ira receber um total de {:.2f}'.format(valorAReceber) + ' reais')