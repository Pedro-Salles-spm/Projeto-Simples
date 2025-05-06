
usuarios = []

while True:
    print("\nMenu:")
    print("1 - Cadastrar usuário")
    print("2 - Ver usuários cadastrados")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do usuário: ")
        idade = input("Digite a idade do usuário: ")
        usuarios.append({"nome": nome, "idade": idade})
        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        if usuarios:
            print("\nUsuários cadastrados:")
            for i, usuario in enumerate(usuarios, start=1):
                print(f"{i}. Nome: {usuario['nome']}, Idade: {usuario['idade']}")
        else:
            print("Nenhum usuário cadastrado ainda.")

    elif opcao == "3":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")