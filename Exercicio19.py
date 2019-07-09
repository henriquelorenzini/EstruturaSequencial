#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanhoArquivo = float(input('Qual o tamanho do arquivo em MB? '))
velocidadeInternet = float(input('Qual a velocidade da sua internet em MBps? '))

tempoDownload = (tamanhoArquivo / velocidadeInternet)/60

print('Seu tempo de download vai ser de {:.2f} minutos'.format(tempoDownload))