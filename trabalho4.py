contatos = []

def mostrar_menu():
    print("\nEntre com a opção desejada:")
    print("1 - Cadastrar Contato")
    print("2 - Consultar Contato(s)")
    print("3 - Remover Contato")
    print("4 - Sair")

def mostrar_menu_contatos():
    print("\nMenu consultar contatos:")
    print("1 - Consultar todos os Contatos")
    print("2 - Consultar por ID")
    print("3 - Consultar por Atividade")
    print("4 - Voltar ao Menu Principal")

def cadastrar():
    # Solicita os dados do contato
    nome = input("Digite o nome do contato: ")
    atividade = input("Digite a atividade do contato: ")
    telefone = input("Digite o telefone do contato: ")

    # Adiciona o contato à lista
    contatos.append({"nome": nome, "atividade": atividade, "telefone": telefone})
    print(f"Contato {nome} cadastrado com sucesso!")

def consultar():
    while True:
        mostrar_menu_contatos()

        opcao_consulta = input("Escolha uma opção de consulta: ")

        if opcao_consulta == "1":
            consultar_todos()
        elif opcao_consulta == "2":
            consultar_por_id()
        elif opcao_consulta == "3":
            consultar_por_atividade()
        elif opcao_consulta == "4":
            break  # Volta ao menu principal
        else:
            print("Opção inválida. Tente novamente.")

def consultar_todos():
    if not contatos:
        print("Não há contatos cadastrados.")
    else:
        print("\nContatos cadastrados:")
        for i, contato in enumerate(contatos, start=1):
            print(f"{i}. Nome: {contato['nome']}, Atividade: {contato['atividade']}, Telefone: {contato['telefone']}")

def consultar_por_id():
    if not contatos:
        print("Não há contatos cadastrados.")
    else:
        try:
            id_contato = int(input("\nDigite o ID do contato que deseja consultar: ")) - 1
            if 0 <= id_contato < len(contatos):
                contato = contatos[id_contato]
                print(f"Nome: {contato['nome']}, Atividade: {contato['atividade']}, Telefone: {contato['telefone']}")
            else:
                print("ID inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número de ID válido.")

def consultar_por_atividade():
    if not contatos:
        print("Não há contatos cadastrados.")
    else:
        atividade = input("\nDigite a atividade que deseja consultar: ")
        encontrados = [contato for contato in contatos if atividade.lower() in contato['atividade'].lower()]
        
        if encontrados:
            print("\nContatos encontrados:")
            for contato in encontrados:
                print(f"Nome: {contato['nome']}, Atividade: {contato['atividade']}, Telefone: {contato['telefone']}")
        else:
            print(f"Nenhum contato encontrado para a atividade: {atividade}")

def remover():
    if not contatos:
        print("Não há contatos para remover.")
    else:
        consultar_todos()
        
        try:
            indice = int(input("\nDigite o número do contato que deseja remover: ")) - 1

            if 0 <= indice < len(contatos):
                contato_removido = contatos.pop(indice)
                print(f"Contato {contato_removido['nome']} removido com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def main():
    while True:
        mostrar_menu()
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            consultar()
        elif opcao == "3":
            remover()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()