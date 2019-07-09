#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido,

salarioHora = float(input('Quanto você recebe por hora? '))
cargaHoraria = int(input('Quantas horas você trabalhou esse mês? '))

salarioBruto = salarioHora * cargaHoraria
impostoRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - inss - sindicato - impostoRenda

print ('Seu salario bruto esse mês foi R${:.2f}'.format(salarioBruto))
print ('Você pagou de imposto de renda R${:.2f}'.format(impostoRenda))
print ('Você pagou ao INSS R${:.2f}'.format(inss))
print ('Você pagou ao sindicato R${:.2f}'.format(sindicato))
print ('Então, com todos os descontos, você recebeu um salario líquido de R${:.2f}'.format(salarioLiquido))