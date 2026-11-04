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
print(f"{map:.2f}")

pr = float(input("Digite a nota da Prova Final: "))
sub = float(input("Digite a nota da Prova Substitutiva: "))

if pr > sub:
    prova_final = pr
    print(f"A Maior nota foi {pr:.2f} ela que vai valer.")
else:
    prova_final = sub
    print(f"A Maior nota foi {sub:.2f} ela que vai valer.")

bonus = float(input("Digite sua nota bônus: "))

nota_final = (map / 0.3) + (prova_final / 0.5) + bonus
print(f"{nota_final:.2f}")

if nota_final >= 6:
    situacao = "Aprovado"
else:
    situacao = "DP"

print(f"Sua situação na matéria de {materia} é de {situacao}")