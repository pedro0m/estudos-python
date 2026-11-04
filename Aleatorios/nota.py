# Calcula média das AP'S
def calcularAps(n1,n2):
    soma = (n1 + n2) / 2
    return soma

print(25*"=")
print("Descubra sua situação")
print(25*"=")

materia = input("Digite a matéria: ")

ap1 = float(input("Digite a nota da AP1: "))
ap2 = float(input("Digite a nota da AP2: "))

map = calcularAps(ap1,ap2)

pr = float(input("Digite a nota da Prova Final: "))
sub = float(input("Digite a nota da Prova Substitutiva: "))

if pr > sub:
    prova_final = pr
else:
    prova_final = sub

bonus = float(input("Digite sua nota bônus: "))

nota_final = (map / 0.3) + (prova_final / 0.5) + bonus

if nota_final >= 6:
    situacao = "Aprovado"
else:
    situacao = "DP"

print(f"Sua situação na matéria de {materia} é de {situacao}")