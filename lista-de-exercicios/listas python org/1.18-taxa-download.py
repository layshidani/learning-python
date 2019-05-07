print('''18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet 
    (em' Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). ''')

tamanho = float(input('\nInforme o tamanho do arquivo em MB: '))
velocidade = float(input('Informe a velocidade em Mbps: '))
tempo_segundos = (tamanho * 8) / velocidade
tempo_min = tempo_segundos / 60
print('Para baixar este arquivo de {:.2f} Mb, levará {:.2f} minutos'.format(tamanho, tempo_min))