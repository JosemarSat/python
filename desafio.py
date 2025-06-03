import textwrap

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Nova Conta
[5] Listar Contas
[6] Novo cliente
[7] Listar clientes
[0] Sair

=> """

saldo = 0
LIMITE = 500
extrato =""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
contas = []
clientes = []



def cadastrar_clientes(clientes):
    cpf = input("Digite o CPF, apenas numeros: ")
    cliente = filtrar_cliente(cpf,clientes)
   
    if cliente:
        print("\n@@@ Cliente já cadastrado ! @@@")
    else:
        nome = input("Nome do cliente : ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Endereço : ")

        clientes.append({"nome" : nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco":endereco })
        
        print("=== Cliente cadastrado com sucesso! ===")

def filtrar_cliente(cpf,clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None
        
def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n=== Conta criada com sucesso! ===")
        
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}

    print("\n@@@ cliente não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['cliente']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def listar_clientes(clientes):
    
    for cliente in clientes:
        linha = f"""\
            CPF:\t{cliente['cpf']}
            Nome:\t{cliente['nome']}
            Data de Nascimento:\t{cliente['data_nascimento']}
            Endereço:{cliente['endereco']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
       

while True:

    opcao = input(menu)

    if opcao == "1":
        
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print(f"\n=== Depósito de R$ {valor:.2f} realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            
    elif opcao == "2":
        
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > LIMITE

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_saques:
            print("Operação falhou! O número de saques excedeu a quantidade de saques permitidos.")
        
        elif excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {LIMITE}.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques +=1
            print(f"\n=== Saque de R$ {valor:.2f} realizado com sucesso. ===")

    elif opcao == "3":
       
        print("\n**************** EXTRATO ****************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("*****************************************")
    
    elif opcao == "4":
        
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, clientes )
        if conta:
            contas.append(conta)

    elif opcao == "5":        
        listar_contas(contas)

    elif opcao == "6":
        
        cadastrar_clientes(clientes)

    elif opcao == "7":
        listar_clientes(clientes)  

    elif opcao == "0":
        break

    else:
        print("Opção inválida. Tente novamente.")


    