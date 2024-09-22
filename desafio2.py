# Desafio 2:
# Precisamos deixar o nosso código mais modularizado, para isso, vamos criar funções
# para as operações existentes: sacar, depositar e visualizar histórico. Além disso,
# para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário
# (cliente do banco) e criar conta corrente (vincular com usuário).

# Requisitos do desafio:

# Operação Depósito: A função depósito deve receber os argumentos apenas por posição
# (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno:
# saldo e extrato

# Operação Saque: A função saque deve receber os argumentos apenas por nome
# # (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques.
# # Sugestão de retorno: saldo e extrato.

# Operação de Extrato: A função extrato deve receber os argumentos por posição e nome
# (positional only e keyword only). Argumentos posicionais: saldo. Argumentos nomeados:
# extrato.

# Precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a vontade
# para adicionar mais funções, exemplo, listar contas.

# Função criar usuário (cliente): Programa deve armazenar os usuários em uma lista,
# um usuário é composto por nome, data de nascimento, CPF e endereço. O endereço é uma string
# com formato; logradouro, n° - bairro - cidade/sigla estado. Deve ser armazenado somente
# os números do CPF (deve ser string). Não podemos cadastrar 2 usuários com o mesmo CPF.

# Criar conta corrente: O programa deve armazenar contas em uma lista, uma conta é composta
# por agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1.
# O número da agência é fixo: "0001". O usuário pode ter mais de uma conta,
# mas uma conta pertence a somente um usuário.

# Dica: Para vincular um usuário a uma conta, filtre a lista de usuários buscando
# o número do CPF informado para cada usuário da lista.

# Bibliotecas
import textwrap


# Função de depósito
def depositar(saldo_conta, valor_deposito, extrato_conta, /):
    try:
        valor_deposito = float(valor_deposito)
        if valor_deposito > 0:
            saldo_conta += valor_deposito
            extrato_conta += f'Depósito: R$ +{valor_deposito:.2f}\n'
            print('Operação realizada com sucesso!')
        else:
            print('Não foi possível completar a operação. Informe um valor acima de zero.')
    except ValueError:
        print("Valor inválido! Por favor, digite um valor numérico.")
    else:
        print(f'Saldo atual: R$ {saldo_conta:.2f}')

    return saldo_conta, extrato_conta

# Função de saque
def sacar(*, valor_saque, saldo_conta, extrato_conta, limite_saque, qnt_saques, limite_saque_diario):
    try:
        valor_saque = float(valor_saque)
        if qnt_saques > limite_saque_diario:
            print('Desculpe, você excedeu o limite de 3 saques diários.')
        elif valor_saque > saldo_conta:
            print('Saldo insuficiente!')
        elif valor_saque > limite_saque:
            print('O valor do saque excede o limite permitido de R$ 500,00.')
        else:
            saldo_conta -= valor_saque
            qnt_saques += 1
            extrato_conta += f'Saque: R$ -{valor_saque:.2f}\n'
            print('Saque realizado com sucesso!')
    except ValueError:
        print("Valor inválido! Por favor, digite um valor numérico.")
    else:
        # Aqui podemos usar o else para confirmar a operação apenas quando tudo ocorre bem
        print(f'Seu saldo atual após o saque é: R$ {saldo_conta:.2f}')
    return saldo_conta, extrato_conta, qnt_saques


# Função para exibir o extrato da conta
def exibe_extrato(saldo_conta, /, *, extrato_conta):
    print('\n================ EXTRATO ================')
    if not extrato_conta:
        print('Não foram realizadas movimentações.')
    else:
        print(extrato_conta)
    print(f'\nSaldo: R$ {saldo_conta:.2f}')
    print('=========================================')


# Função que busca os clientes por CPF
def filtrar_cliente(lista_de_clientes, cpf_cliente):
    if not cpf_cliente:
        return None
    return next((cliente for cliente in lista_de_clientes if cliente['CPF'] == cpf_cliente), None)


# Função que filtra contas por número de conta
def filtrar_conta(lista_de_contas_correntes, num_conta):
    for conta in lista_de_contas_correntes:
        if conta['numero_conta'] == int(num_conta):
            return conta
    return None

# Função que valida o CPF no formato correto
def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido! Deve conter 11 dígitos numéricos.")
        return False
    return True

# Função de coleta o endereço para ser usado na função adicionar_cliente()
def coletar_endereco():
    print('Endereço completo:\n')
    logradouro = input('Rua/Avenida: ')
    num_casa = input('N°: ')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    sigla_estado = input('Sigla do Estado (ex: SP, RJ): ')
    return f'{logradouro}, {num_casa} - {bairro} - {cidade}/{sigla_estado}'

# Função que adiciona um novo cliente
def adicionar_cliente(lista_de_clientes):
    cpf = input('Informe o CPF (apenas números) do cliente: ')
    if not validar_cpf(cpf):
        return

    usuario = filtrar_cliente(lista_de_clientes, cpf)
    if usuario:
        print('Este CPF já está cadastrado!')
        return

    nome = input('Nome: ')
    data_nascimento = input('Data de nascimento (dia-mês-ano): ')
    endereco = coletar_endereco()

    cliente = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'CPF': cpf,
        'endereco': endereco
    }

    print('Cliente criado com sucesso!')
    return cliente


# Função que cria conta corrente
def criar_conta_corrente(lista_de_clientes, num_contas, AGENCIA):
    cpf = input('Informe o CPF (apenas números) do cliente: ')
    usuario = filtrar_cliente(lista_de_clientes, cpf)

    if not usuario:
        print('Este CPF não está cadastrado!')
        return

    num_conta_corrente = num_contas + 1
    conta_corrente = {
        'agencia': AGENCIA,
        'numero_conta': num_conta_corrente,
        'usuario': usuario
    }

    print('Conta corrente criada com sucesso!')
    return conta_corrente


# Função que exclui contas da lista de contas
def excluir_conta_corrente(lista_de_contas_corrente, lista_de_clientes):
    print('\n================ Excluir Conta ================\n')
    menu = """
    Escolha uma das opções abaixo:

    [c]  Excluir usando CPF
    [n]  Excluir usando número da conta
    [l]  Listar contas por CPF
    [v]  Voltar para Menu Principal

    Opção: """

    while True:
        opcao = input(menu)
        if opcao.lower() == 'c':
            cpf = input('Informe o CPF (apenas números) ou digite v para voltar: ')

            # Retorna ao menu
            if cpf.lower() == 'v':
                return
            
            usuario = filtrar_cliente(lista_de_clientes, cpf)
            
            if not usuario:
                print('Este CPF não está cadastrado!')
                return

            for conta in lista_de_contas_corrente:
                if conta['usuario']['CPF'] == cpf:
                    lista_de_contas_corrente.remove(conta)
                    print('Conta-corrente excluída com sucesso!')
                else:
                    print('Não há contas correntes atreladas a este CPF!')

        elif opcao.lower() == 'n':
            numero_conta = input('Informe o número da conta ou digite v para voltar: ')

            # Retorna ao menu
            if cpf.lower() == 'v':
                return

            conta = filtrar_conta(lista_de_contas_corrente, numero_conta)
            
            if not conta:
                print('Esta conta não existe!')
                return

            lista_de_contas_corrente.remove(conta)
            print('Conta-corrente excluída com sucesso!')

        elif opcao.lower() == 'l':
            cpf = input('Informe o CPF (apenas números) do cliente: ')
            print(listar_contas(lista_de_contas_corrente, cpf))

        elif opcao.lower() == 'v':
            return
def listar_contas(lista_de_contas, cpf_do_cliente):

    for contas in lista_de_contas:
        if cpf_do_cliente == contas['usuario']['CPF']:
            linha = f"""\
            Agência:\t{contas['agencia']}
            Conta_corrente:\t{contas['numero_conta']}
            Titular:\t{contas['usuario']['nome']} - {str(contas['usuario']['CPF'])}
            """
            print('#' * 100)
            print(textwrap.dedent(linha))
        else:
            print('Nenhuma conta foi encontrada!')


# Função principal
def main():
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    contas_corrente = []
    clientes = []
    contador_contas = 0

    while True:
        opcao = menu()

        if opcao.lower() == 'd':
            print('\n================ DEPÓSITO ================\n')
            deposito = input('Informe o valor do depósito (ou digite "v" para retornar ao menu): ')
            if deposito.lower() == 'v':
                continue
            saldo, extrato = depositar(saldo, deposito, extrato)

        elif opcao.lower() == 's':
            print('\n================ SAQUE ================\n')
            valor = input('Informe o valor do saque (ou digite "v" para retornar ao menu): ')
            if valor.lower() == 'v':
                continue
            saldo, extrato, numero_saques = sacar(
                saldo_conta=saldo,
                valor_saque=valor,
                extrato_conta=extrato,
                limite_saque=limite,
                qnt_saques=numero_saques,
                limite_saque_diario=LIMITE_SAQUES
            )

        elif opcao.lower() == 'e':
            exibe_extrato(saldo, extrato_conta=extrato)

        elif opcao.lower() == 'c':
            nova_conta = criar_conta_corrente(clientes, contador_contas, AGENCIA)
            if nova_conta:
                contas_corrente.append(nova_conta)
                contador_contas += 1

        elif opcao.lower() == 'n':
            novo_cliente = adicionar_cliente(clientes)
            if novo_cliente:
                clientes.append(novo_cliente)

        elif opcao.lower() == 'ec':
            excluir_conta_corrente(contas_corrente, clientes)

        elif opcao.lower() == 'sa':
            print('Encerrando o sistema...')
            break

        else:
            print('Opção inválida. Digite d - Depósito, s - Saque, e - Extrato, sa - Sair')


# Menu de opções do sistema
def menu():
    menu = """
    #####################################################
            Olá! Seja Bem-Vindo ao Banco ByteBank!
    #####################################################

    Escolha uma das opções abaixo:

    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [c]  Abrir Conta Corrente
    [n]  Novo Cliente
    [ec] Excluir Conta
    [sa] Sair

    Opção: """
    return input(textwrap.dedent(menu))

if __name__ == '__main__':
    main()

