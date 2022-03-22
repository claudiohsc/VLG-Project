import csv
import keyboard
#Importa biblioteca para trabalhar com arquivos csv: tabelas para excel.

fields = ['Nome', 'CPF', 'Documentos', 'Etapa', 'Unidade']
#Determina as colunas da tabela.

rows = []

while True:
    lista = []
    lista.append(str(input('Digite o nome: '))) #Recebe as informações e guarda em uma lista.
    lista.append(str(input('Digite o CPF: ')))
    lista.append(str(input('Digite a quantidade de procurações: ')))
    lista.append(str(input('Digite a etapa: ')))
    lista.append(str(input('Digite a unidade: ')))
    
    rows.append(lista)
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
    

print(lista)
print(rows)



'''
rows = [ ['Maria', '12345678900', '2', 'Gardenia', '17'],   
         ['Jose', '12345678900', '2', 'Jacarandas', '58'],   
         ['Paulo', '12345678900', '2', 'Pitangueiras', '23'],   
         ['Carlos', '12345678900', '1', 'Orquideas', '35'],   
         ['Ana', '12345678900', '1', 'Bougainville', '90'],   
         ['Clara', '12345678900', '2', 'Azaleias', '13']]   
#Determina as linhas da tabela em uma lista seguindo as colunas.

filename = "dados.csv"
#Declara o nome e extensão do arquivo de saída.

with open(filename, 'w') as csvfile:   
    
    csvwriter = csv.writer(csvfile)   #Abre o arquivo e começa a escrever.
          
    
    csvwriter.writerow(fields)   #colunas
          
    
    csvwriter.writerows(rows) #linhas
'''