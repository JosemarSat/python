import textwrap
from datetime import datetime

menu = """
================ MENU ================ 
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
LIMITE = 5000
extrato =""
numero_depositos = 0
numero_saques = 0
CHEQUE_ESPECIAL = 2000
LIMITE_TRANSACOES = 10
AGENCIA = "0001"
contas = []
clientes = []
datamov=""
mascara_ptbr = "%d/%m/%Y %H:%M:%S"   

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
        input("Pressione qquer tecla para continuar...")
        
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
        input("Pressione qquer tecla para continuar...")        


while True:
    
    opcao = input(menu)

    if opcao == "1":
        
        data = datetime.now()
        datamov = data.strftime(mascara_ptbr)        
        excedeu_transacoes = numero_saques + numero_depositos >= LIMITE_TRANSACOES
        valor = float(input("Informe o valor do depósito: "))
        
        if excedeu_transacoes:
            
            print("Operação falhou! Excedeu a quantidade de transações permitidas.")
                        
        if valor > 0:
            
            saldo += valor
            extrato += f"\nData:{datamov}"
            extrato += f"\t\t\tR$ {valor:.2f}" 
            if not excedeu_transacoes:
                
                numero_depositos += 1
                print(f"\n=== Depósito de R$ {valor:.2f} realizado com sucesso! ===")
            
        else:
            
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        input("Pressione qquer tecla para continuar...")
    
    elif opcao == "2":
        
        data = datetime.now()
        datamov = data.strftime(mascara_ptbr)       
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo + CHEQUE_ESPECIAL
        excedeu_limite = valor > LIMITE
        excedeu_transacoes = numero_saques + numero_depositos >= LIMITE_TRANSACOES

        if excedeu_saldo:
        
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_transacoes:
            
            print("Operação falhou! Excedeu a quantidade de transações permitidas.")
        
        elif excedeu_limite:
           
            print(f"Operação falhou! O valor do saque excede o limite de R$ {LIMITE}.")
            
        elif valor > 0:
            
            saldo -= valor
            extrato += f"\nData:{datamov}"
            extrato += f"\tR$ {valor:.2f}" 
            numero_saques +=1
            print(f"\n=== Saque de R$ {valor:.2f} realizado com sucesso. ===")
        input("Pressione qquer tecla para continuar...")
        
    elif opcao == "3":
        
        data = datetime.now()
        datamov = data.strftime(mascara_ptbr)
        
        print("\n***********************************************************")
        print("      DATA                       DÉBITOS        CRÉDITOS   ")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        
        if saldo > 0:
            
            print(f"Saldo:\t\t\t\t\t\tR$ {saldo:.2f}")
            
        else:
            
            print(f"Saldo: \tR$ {saldo:.2f}")
            
        print(f"Limite do Cheque Especial:\t\t\tR$ {CHEQUE_ESPECIAL:.2f}")
        print(f"Saldo disponível:\t\t\t\tR$ {CHEQUE_ESPECIAL + saldo:.2f}")
        print(f"Você ainda tem {LIMITE_TRANSACOES - (numero_saques + numero_depositos)} transações disponíveis para hoje!")
        print(f"Extrato emitido em: {datamov}")
        print("***********************************************************")
        input("Pressione qquer tecla para continuar...")
        
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


    
    