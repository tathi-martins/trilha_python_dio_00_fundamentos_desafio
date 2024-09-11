# Criando um sistema de banco simples com apenas três operações:
# depósito, saque e extrato. A versão 1 terá apenas um usuário. Não
# será necessário identificar os usuários, a agência e a conta bancária.

# Requisitos do desafio:

# Operação Depósito: Todos os depósito devem ser armazenados em uma variável e
# exibidos na operação de extrato.

# Operação Saque: O sistema deve permitir realizar 3 saques diários
# com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha
# saldo em conta, o sistema deve exibir uma mensagem informando que
# não será possível sacar o dinheiro por saldo insuficiente. Todos os
# saques devem ser armazenadados em uma variável e exibidos na operação
# de extrato

# Operação de Extrato: Deve listar todos os depósitos e saques realizados
# na conta. No fim da listagem deve ser exibido o saldo atual da conta.
# Os valores devem exibidos utilizando o formato R$ xxx.xx, exemplo:
# 1500.45 -> R$ 1500.45

# Função para realizar o depósito
def depositar(valor_deposito, saldo_conta):
    saldo_conta += valor_deposito
    return saldo_conta  # Retorna o novo saldo

# Função para realizar o saque
def sacar(valor_saque, saldo_conta, limite_saques, qnt_saques, limite_saque_diario):
    # Verifica se o número de saques diários foi excedido
    if qnt_saques >= limite_saque_diario:
        print('Desculpe, mas você excedeu o limite de três saques diários.')
    # Verifica se há saldo suficiente na conta
    elif valor_saque > saldo_conta:
        print('Operação Inválida! Saldo Insuficiente!')
    # Verifica se o valor do saque é maior que o limite por saque
    elif valor_saque > limite_saques:
        print('Desculpe, mas o limite do saque é de até R$ 500,00.')
    else:
        saldo_conta -= valor_saque
        qnt_saques += 1  # Incrementa o número de saques realizados
        return saldo_conta, qnt_saques, True  # Retorna o saldo atualizado, número de saques e sucesso da operação
    return saldo_conta, qnt_saques, False  # Retorna sem alterações se o saque falhar

# Função para exibir o extrato da conta
def exibe_extrato(saldo_conta, extrato_conta):
    print('\n================ EXTRATO ================')
    # Verifica se há movimentações registradas
    if not extrato_conta:
        print('Não foram realizadas movimentações.')
    else:
        print(extrato_conta)  # Exibe o extrato das transações
    print(f'\nSaldo: R$ {saldo_conta:.2f}')
    print('==========================================')

# Menu de opções do sistema
menu = """
#####################################################
        Olá! Seja Bem-Vindo ao Banco ByteBank!
#####################################################

Escolha uma das opções abaixo:

[d]  Depositar
[s]  Sacar
[e]  Extrato
[sa] Sair

Opção: """

# Variáveis iniciais
saldo = 0  # Saldo inicial
limite = 500  # Limite por saque
extrato = ''  # Registro das movimentações
numero_saques = 0  # Contagem de saques realizados
LIMITE_SAQUES = 3  # Limite de saques por dia

# Loop principal do sistema
while True:
    opcao = input(menu)  # Solicita a escolha da operação

    # Operação de depósito
    if opcao.lower() == 'd':
        print('\n================ DEPÓSITO ================\n')
        deposito = input('Informe o valor do depósito (ou digite "v" para retornar ao menu): ')

        if deposito.lower() == 'v':  # Permite voltar ao menu
            continue

        deposito = float(deposito)  # Converte o valor para float
        if deposito > 0:
            saldo = depositar(deposito, saldo)  # Atualiza o saldo
            extrato += f'Depósito: R$ +{deposito:.2f}\n'  # Adiciona o depósito ao extrato
            print('Operação realizada com sucesso!')
        else:
            print('Não foi possível completar a operação. Informe um valor acima de zero.')

        input("Pressione Enter para continuar...")  # Pausa para o usuário visualizar a mensagem

    # Operação de saque
    elif opcao.lower() == 's':
        print('\n================ SAQUE ================\n')
        valor = input('Informe o valor do saque (ou digite "v" para retornar ao menu): ')

        if valor.lower() == 'v':  # Permite voltar ao menu
            continue

        valor = float(valor)  # Converte o valor para float
        saldo, numero_saques, saque_realizado = sacar(valor, saldo, limite, numero_saques, LIMITE_SAQUES)

        if saque_realizado:
            extrato += f'Saque: R$ -{valor:.2f}\n'  # Adiciona o saque ao extrato
            print('Operação realizada com sucesso!')

        input("Pressione Enter para continuar...")  # Pausa para o usuário visualizar a mensagem

    # Operação de extrato
    elif opcao.lower() == 'e':
        exibe_extrato(saldo, extrato)  # Exibe o extrato
        input("Pressione Enter para continuar...")  # Pausa para o usuário visualizar o extrato

    # Sai do loop e encerra o programa
    elif opcao.lower() == 'sa':
        break

    # Opção inválida
    else:
        print('Opção inválida. Digite d - Depósito, s - Saque, e - Extrato, sa - Sair')
