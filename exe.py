agenda = {}

def incluir_novo_nome(nome, telefones):
    agenda[nome] = telefones

def incluir_telefone(nome, telefone):
    if nome in agenda:
        agenda[nome].append(telefone)
    else:
        resposta = input(f"{nome} NÃO ESTÁ NA AGENDA. DESEJA INCLUIR? (s/n): ")
        if resposta.lower() == 's':
            incluir_novo_nome(nome, [telefone])

def excluir_telefone(nome, telefone):
    if nome in agenda:
        if telefone in agenda[nome]:
            agenda[nome].remove(telefone)
            if not agenda[nome]:
                excluir_nome(nome)
        else:
            print(f"TELEFONE {telefone} NÃO ENCONTRADO PARA {nome}.")
    else:
        print(f"{nome} NÃO ESTÁ NA AGENDA.")

def excluir_nome(nome):
    if nome in agenda:
        del agenda[nome]
    else:
        print(f"{nome} NÃO ESTÁ NA AGENDA.")

def consultar_telefone(nome):
    if nome in agenda:
        print(f"Nome: {nome} | Telefones: {', '.join(agenda[nome])}")
    else:
        print(f"{nome} NÃO ESTÁ NA AGENDA.")
        resposta = input("DESEJA INCLUIR UM NOVO NOME? (s/n): ")
        if resposta.lower() == 's':
            telefone = input(f"Informe o telefone para {nome}: ")
            incluir_novo_nome(nome, [telefone])

def menu():
    while True:
        opcao = input("Escolha uma opção: [1] Consultar Telefone, [2] Incluir Telefone, [3] Excluir Telefone, [4] Excluir Nome, [5] Sair: ")
        
        if opcao == '1':
            nome = input("Digite o nome para consultar: ")
            consultar_telefone(nome)
        
        elif opcao == '2':
            nome = input("Digite o nome para adicionar telefone: ")
            telefone = input("Digite o telefone: ")
            incluir_telefone(nome, telefone)
        
        elif opcao == '3':
            nome = input("Digite o nome para excluir telefone: ")
            telefone = input("Digite o telefone: ")
            excluir_telefone(nome, telefone)
        
        elif opcao == '4':
            nome = input("Digite o nome para excluir: ")
            excluir_nome(nome)
        
        elif opcao == '5':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida, tente novamente.")

incluir_novo_nome('João', ['1234-5678', '9876-5432'])
menu()
