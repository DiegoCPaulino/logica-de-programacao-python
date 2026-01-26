# Listas que armazenam os dados de dentistas e pacientes
dentistas = []
pacientes = []

# Credenciais do administrador do sistema
usuarioAdmin = "useradm"
senhaAdmin = "adm123"

# Função para cadastro de pacientes
def cadastroPaciente():
    while True:
        paciente = {}  # Dicionário que armazenará os dados do paciente

        # Interface visual do formulário
        print("\n" + "="*40)
        print("        CADASTRO DE PACIENTE")
        print("="*40)

        # Captura de dados do paciente
        paciente["nomeCompleto"] = input("Nome completo: ")
        paciente["cpf"] = input("CPF (somente números): ")
        paciente["telefone"] = input("Telefone (somente números): ")
        paciente["email"] = input("E-mail: ")

        # Exibe os dados fornecidos para conferência
        print("\n" + "-"*40)
        print("DADOS FORNECIDOS:")
        for chave, valor in paciente.items():
            print(f"{chave:15}: {valor}")
        print("-"*40)

        # Confirmação antes de adicionar o paciente à lista
        confirmar = input("\nTem certeza que deseja adicionar esse paciente ao sistema?"
                          "\n1 - Confirmar e adicionar"
                          "\n2 - Refazer formulário"
                          "\n3 - Cancelar e voltar ao menu principal"
                          "\nDigite sua escolha: ")
        if confirmar == "1":
            pacientes.append(paciente)  # Adiciona paciente à lista
            print(f"\n>>> Paciente {paciente['nomeCompleto']} cadastrado com sucesso!")
        elif confirmar == "2":
            continue  # Recomeça o loop para refazer o formulário
        elif confirmar == "3":
            break  # Sai da função e retorna ao menu principal
        else:
            print("\nOpção inválida. Voltando ao menu principal...")
            break

        # Pergunta o que o usuário deseja fazer em seguida
        opcao = input("\nO que deseja fazer agora?"
                      "\n1 - Cadastrar outro paciente"
                      "\n2 - Voltar ao menu principal"
                      "\n0 - Sair do sistema"
                      "\nDigite sua escolha: ")
        if opcao == "1":
            continue
        elif opcao == "2":
            break
        elif opcao == "0":
            print("\nSaindo do sistema... Até logo!")
            return
        else:
            print("\nOpção inválida! Voltando ao menu principal...")
            break

# Função para cadastro de dentistas
def cadastroDentista():
    while True:
        dentista = {}  # Dicionário para armazenar os dados do dentista

        # Interface visual do formulário
        print("\n" + "="*40)
        print("       CADASTRO DE DENTISTA")
        print("="*40)

        # Captura de dados do dentista
        dentista["nomeCompleto"] = input("Nome completo: ")
        dentista["cpf"] = input("CPF (somente números): ")
        dentista["numeroCro"] = input("Número do CRO (somente números): ")
        dentista["telefone"] = input("Telefone (somente números): ")
        dentista["email"] = input("E-mail: ")
        dentista["especialidade"] = input("Especialidade: ")

        # Exibe os dados fornecidos para conferência
        print("\n" + "-"*40)
        print("DADOS FORNECIDOS:")
        for chave, valor in dentista.items():
            print(f"{chave:15}: {valor}")
        print("-"*40)

        # Confirmação antes de adicionar o dentista à lista
        confirmar = input("\nTem certeza que deseja adicionar esse dentista ao sistema?"
                          "\n1 - Confirmar e adicionar"
                          "\n2 - Refazer formulário"
                          "\n3 - Cancelar e voltar ao menu principal"
                          "\nDigite sua escolha: ")
        if confirmar == "1":
            # Geração automática de usuário e senha
            dentista["usuario"] = gerarUsuario(dentista["nomeCompleto"])
            dentista["senha"] = gerarSenha(dentista["nomeCompleto"], dentista["numeroCro"])
            dentistas.append(dentista)
            print(f"\n>>> Dentista {dentista['nomeCompleto']} cadastrado com sucesso!")
            print(f"Usuário: {dentista['usuario']}")
            print(f"Senha:   {dentista['senha']}")
        elif confirmar == "2":
            continue  # Recomeça o loop para refazer o formulário
        elif confirmar == "3":
            break  # Sai da função e retorna ao menu principal
        else:
            print("\nOpção inválida. Voltando ao menu principal...")
            break

        # Pergunta o que o usuário deseja fazer em seguida
        opcao = input("\nO que deseja fazer agora?"
                      "\n1 - Cadastrar outro dentista"
                      "\n2 - Voltar ao menu principal"
                      "\n0 - Sair do sistema"
                      "\nDigite sua escolha: ")
        if opcao == "1":
            continue
        elif opcao == "2":
            break
        elif opcao == "0":
            print("\nSaindo do sistema... Até logo!")
            return
        else:
            print("\nOpção inválida! Voltando ao menu principal...")
            break

# Função que gera o nome de usuário do dentista automaticamente
def gerarUsuario(nome):
    primeiroNome = nome.split()[0].lower()  # Pega apenas o primeiro nome e transforma em minúsculo
    numero = str(len(dentistas) + 1)       # Adiciona um número sequencial
    return primeiroNome + numero

# Função que gera a senha do dentista automaticamente
def gerarSenha(nome, cro):
    primeiroNome = nome.split()[0].lower()
    return primeiroNome + cro  # Combina o primeiro nome com o número do CRO

# Loop principal do sistema
while True:
    print("\n" + "="*50)
    print("          SISTEMA DE CADASTRO TdB")
    print("="*50)

    # Menu principal com opções para dentista, paciente ou exibição de dados
    menuPrincipal = input(
        "\nEscolha uma opção:"
        "\n1 - Ser um dentista voluntário"
        "\n2 - Ser um paciente da TdB"
        "\n3 - Exibir dentistas cadastrados (acesso restrito)"
        "\n4 - Exibir pacientes cadastrados (acesso restrito)"
        "\n0 - Sair do sistema"
        "\nDigite sua escolha: "
    )

    if menuPrincipal == "1":
        cadastroDentista()  # Chama a função de cadastro de dentista

    elif menuPrincipal == "2":
        cadastroPaciente()  # Chama a função de cadastro de paciente

    elif menuPrincipal == "3":
        # Acesso restrito: somente administrador
        user = input("\nUsuário admin: ")
        senha = input("Senha admin: ")
        if user == usuarioAdmin and senha == senhaAdmin:
            print("\n" + "="*40)
            print("      LISTA DE DENTISTAS CADASTRADOS")
            print("="*40)
            if dentistas:
                for d in dentistas:
                    print(f"Nome: {d['nomeCompleto']:20} | CPF: {d['cpf']:11} | CRO: {d['numeroCro']}")
            else:
                print("Nenhum dentista cadastrado ainda.")
        else:
            print("\nUsuário ou senha incorretos. Acesso negado.")

    elif menuPrincipal == "4":
        # Acesso restrito: administrador ou dentista
        user = input("\nUsuário: ")
        senha = input("Senha: ")
        if user == usuarioAdmin and senha == senhaAdmin:
            print("\n" + "="*40)
            print("       LISTA DE PACIENTES CADASTRADOS")
            print("="*40)
            if pacientes:
                for p in pacientes:
                    print(f"Nome: {p['nomeCompleto']:25} | CPF: {p['cpf']}")
            else:
                print("Nenhum paciente cadastrado ainda.")
        else:
            # Verifica se o usuário é um dentista cadastrado
            encontrado = False
            for d in dentistas:
                if d["usuario"] == user and d["senha"] == senha:
                    encontrado = True
                    print(f"\nBem-vindo Dr(a). {d['nomeCompleto']}!")
                    print("\n" + "="*40)
                    print("       LISTA DE PACIENTES CADASTRADOS")
                    print("="*40)
                    if pacientes:
                        for p in pacientes:
                            print(f"Nome: {p['nomeCompleto']:25} | CPF: {p['cpf']}")
                    else:
                        print("Nenhum paciente cadastrado ainda.")
                    break

            if not encontrado:
                print("\nUsuário ou senha incorretos. Acesso negado.")

    elif menuPrincipal == "0":
        print("\nSaindo do sistema... Até logo!")
        break  # Sai do loop principal e encerra o programa

    else:
        print("\nOpção inválida. Tente novamente.")  # Caso o usuário digite uma opção inexistente
