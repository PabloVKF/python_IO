arquivo_contatos = open('dados/contatos.csv', encoding='latin_1')

for row in arquivo_contatos:
    print(row, end='')
