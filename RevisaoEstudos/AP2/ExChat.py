'''nome = input('Digite o nome do aluno: ') # Recebe o nome do aluno

notas = []  # Lista que vai ser preenchida com a iteração abaixo
for i in range(4) : 
    i += 1
    nota = float(input(f'Digite a {i}° nota: '))
    notas.append(nota)

falta = int(input('Quantas faltas: ')) # quantidade de faltas do aluno

soma = 0
for n in notas : # soma a quantidade de notas e devolve a media
    soma += n
media = soma / len(notas)

if falta > 10 : # situação do aluno
    situacao = 'Reprovado por falta'
elif media < 5 and falta <= 10 :
    situacao = 'Reprovado por nota'
elif media < 7:
    situacao = 'Recuperação'
else:
    situacao = 'Aprovado'

maior_nota = notas[0]
menor_nota = notas[0]
for nota in notas: # descobre a maior e a menor nota
    if nota > maior_nota:
        maior_nota = nota

    if nota < menor_nota:
        menor_nota = nota

print(f'Olá {nome}, suas notas foram: {notas}')
print(f'sua média foi de: {media:.2f}')
print(f'sua maior nota: {maior_nota}')
print(f'sua menor nota: {menor_nota}')
print(f'sua situação: {situacao}')'''

'''estoque = {
    "Mouse": 15,
    "Teclado": 8,
    "Monitor": 3,
    "Headset": 12,
    "Webcam": 2
}

for nome, qtde in estoque.items() :
    print(f'Nome: {nome}, Quantidade: {qtde}')

for nome, qtde in estoque.items() :
    if qtde < 5 :
        print(f'O produto: {nome}, tem a quantidade de: {qtde} que é menor que 5')

soma = 0
for p, q in estoque.items() :
    soma += q
print(f'A quantidade total de produtos no estoque é de {soma}')

maior = 0
for p, q in estoque.items():
    if q > maior:
        maior = q
        produto = p
print(f'O produto com maior quantidade é: {produto} com quantidade de: {maior}')

estoque_maior = {chave: valor for chave, valor in estoque.items() if valor >= 10}
print(estoque_maior)'''

# chat fez

'''alunos_python = {
    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo"
}

alunos_sql = {
    "Bruno", "Daniela", "Fernanda", "Gabriel", "Ana"
}

notas = (
    ("Ana", 9.0),
    ("Bruno", 6.5),
    ("Carlos", 8.0),
    ("Daniela", 7.5),
    ("Eduardo", 4.0),
    ("Fernanda", 8.5),
    ("Gabriel", 5.0)
)

# 1. Participaram das duas atividades
ambas = alunos_python & alunos_sql

# 2. Participaram somente de Python
somente_python = alunos_python - alunos_sql

# 3. Participaram de pelo menos uma atividade
todos = alunos_python | alunos_sql

# 4. Alunos com nota maior ou igual a 7
aprovados = [
    nome for nome, nota in notas
    if nota >= 7
]

# 5. Alunos das duas atividades com nota >= 7
aprovados_ambas = {
    nome: nota for nome, nota in notas
    if nome in ambas and nota >= 7
}

print("Participaram de ambas:", ambas)
print("Somente Python:", somente_python)
print("Todos os participantes:", todos)
print("Alunos aprovados:", aprovados)
print("Aprovados em ambas:", aprovados_ambas)'''