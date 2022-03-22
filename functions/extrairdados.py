import csv
import keyboard
#Importa biblioteca para trabalhar com arquivos csv: tabelas para excel.

colunas = ['Nome', 'CPF', 'Documentos', 'Etapa', 'Unidade']
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


filename = "dados.csv"
#Declara o nome e extensão do arquivo de saída;

with open(filename, 'w') as csvfile:   
    
    csvwriter = csv.writer(csvfile)   #Abre o arquivo e começa a escrever;
          
    
    csvwriter.writerow(colunas)   #escreve as colunas;
          
    
    csvwriter.writerows(rows) #escreve as linhas;
