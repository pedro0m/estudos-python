"""notas = [7.5, 4.0, 9.0, 6.5, 8.0]

# fazer um loop com o for onde o i representa a nota e usar print pra mostrar essa nota
for i in notas :
    print( i )

# criar uma variavel que vai armazenar a contagem e um loop que percorre a lista com um filtro que se nota for < 6 impede de atualizar o contador
contador = 0
for i in notas :
    if i >= 6 :
        contador += 1

print(contador)

# uma variavel que guarda o valor de todas as notas somadas por um loop para usar no calculo da media notas somadas divididas pela quantidade na lista
soma_notas = 0
for i in notas :
    soma_notas += i

media = soma_notas / len(notas)
print(media)

# uma variavel pra guardar a quantidade de alunos que estão abaixo da media e um loop com um filtro dentro para descobrir quais são

abaixo_media = 0
for i in notas :
    if i < media :
        abaixo_media += 1

print(abaixo_media)"""

'''precos = [120, 85, 300, 45, 150, 70, 220]

# variavel pra guardar o ultimo maior e loop pra percorrer a lista filtrando os maiores que os anteriores
maior = 0
for preco in precos :
    if preco > maior :
        maior = preco
        
print(maior)

# menor recebe o ultimo preco que foi considerado maior e faz exatamente o contrario do loop anterior
menor = maior
for preco in precos :
    if preco < menor :
        menor = preco

print(menor)

# mesmo raciocionio que o das notas
soma_preco = 0
for preco in precos :
    soma_preco += preco

media_preco = soma_preco / len(precos)

print(media_preco)

# utilizando a lista vazia para receber os precos maiores que a media
acima_media = []
for preco in precos :
    if preco > media_preco :
        acima_media.append(preco)

print(acima_media)

# utilizando o contador e utilizando a logica de que se preco for maior ou igual a 80 e menor ou igual a 200 a variavel recebe uma contagem
contador = 0
for preco in precos :
    if preco >= 80 and preco <= 200 :
        contador += 1

print(contador)'''

alunos = [
    {"nome": "Ana", "nota": 8.5, "faltas": 2},
    {"nome": "Carlos", "nota": 5.0, "faltas": 8},
    {"nome": "Mariana", "nota": 9.0, "faltas": 1},
    {"nome": "Lucas", "nota": 6.5, "faltas": 5},
    {"nome": "Pedro", "nota": 4.0, "faltas": 10}
]


# aluno recebe o dicionario no primeiro loop e o proximo loop acessa esse dicionario filtrando a chave se chave for nome do aluno
for aluno in alunos :
    for chave in aluno :
        if chave == "nome" :
            print(aluno[chave])

notas_maiores = []
for aluno in alunos :
    for chave in aluno :
        nota = aluno["nota"]
        if chave == "nome" and nota >= 7 :
            notas_maiores.append(aluno[chave])

print(notas_maiores)