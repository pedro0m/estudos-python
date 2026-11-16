frota = [
    {'placa': 'ABC1234', 'modelo': 'Kwid', 'categoria': 'Economico', 'disponivel': True, 'diaria': 90.0},
    {'placa': 'XYZ9876', 'modelo': 'Corolla', 'categoria': 'Sedan', 'disponivel': False, 'diaria': 250.0},
    {'placa': 'DEF5678', 'modelo': 'Onix', 'categoria': 'Economico', 'disponivel': True, 'diaria': 100.0},
    {'placa': 'GHI9012', 'modelo': 'Compass', 'categoria': 'SUV', 'disponivel': True, 'diaria': 300.0},
    {'placa': 'JKL3456', 'modelo': 'Mobi', 'categoria': 'Economico', 'disponivel': False, 'diaria': 80.0}
]

'''frota_atualizada = [] # Lista vazia para receber o veiculo com seguro

for veiculo in frota : # procura cada veiculo dentro da lista frota
    if veiculo["disponivel"] : 
        taxa = veiculo["diaria"] * 0.1 # taxa do seguro é de 10% do valor da diaria
        veiculo["seguro"] = taxa
        frota_atualizada.append(veiculo) # frota atualizada recebe veiculo com o seguro

for veiculo in frota_atualizada :
    if veiculo["categoria"] == "Economico" :
        total = veiculo["diaria"] + veiculo["seguro"] # guarda o total do seguro
        print("Modelo:" , veiculo["modelo"], ", Total:" , total)

modelos_disponiveis = [veiculo["modelo"] for veiculo in frota if veiculo["disponivel"]]

resumo_disponiveis = [{"modelo": veiculo["modelo"], "total": veiculo["diaria"] * 1.1} for veiculo in frota if veiculo["disponivel"]]


economicos_disponiveis = [veiculo["modelo"] for veiculo in frota if veiculo["disponivel"] and veiculo["categoria"] == "Economico"]


diarias_promocionais = [veiculo['diaria'] * 0.9 if veiculo['categoria'] == 'Economico' else veiculo['diaria'] for veiculo in frota]
'''
valores_disponiveis = [veiculo['diaria'] * 1.15 if veiculo['diaria'] >= 200 else veiculo['diaria'] for veiculo in frota if veiculo['disponivel']]

print(valores_disponiveis)