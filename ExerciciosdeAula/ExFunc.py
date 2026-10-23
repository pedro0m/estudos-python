'''
def saudar(nome, hora):
    if hora >= 0 and hora <= 23:
        if hora < 12:
            print(f'Bom dia {nome}!')
        elif hora < 18:
            print(f'Boa tarde {nome}!')
        else:
            print(f'Boa noite {nome}!')

saudar(input('Nome: '),int(input('Hora: ')))
'''

def calcular_dobro(numero):
    numero = numero * 2
    print(float(numero))

calcular_dobro()