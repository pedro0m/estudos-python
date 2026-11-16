def menu() :
    while True :
        print("""[ 1 ] - Adicionar Contato
[ 2 ] - Remover Contato
[ 3 ] - Buscar Contato
[ 4 ] - Listar Contatos ( A - Z )
[ 5 ] - Estatísticas de E-mail
[ 6 ] - Sair""")
        opc = input("Digite uma opção: ")
        if opc in ['1','2','3','4','5','6'] :
            return opc
        else :
            print("Você digitou", opc, "Esta opção está inválida.")

def adicionar_contato(nome, telefone, email) :
    if telefone in telefones_cadastrados :
        print("Telefone já cadastrado.")
    else :
        "c"

agenda_contatos = {
    "Ana Silva": ("99999-1111", "ana@empresa.com"),          
    "Bruno Costa": ("98888-2222", "bruno@gmail.com"),
    "Carla Dias": ("97777-3333", "carla@empresa.com")
    }

telefones_cadastrados = {"99999-1111", "98888-2222", "97777-3333"}
