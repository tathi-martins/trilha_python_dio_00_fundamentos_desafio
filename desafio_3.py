# Desafio 3

# Objetivo Geral: Iniciar a modelagem do sistema bancário em POO. Adicionar classes para cliente e as operações
# bancárias: depósito e saque. Atualizar a implementação do sistema bancário, para armazenar os dados de clientes
# e contas bancárias em objetos em vez de dicionários. O código deve seguir o modelo de classes UML a seguir:

# Desafio Extra: Após concluir a modelagem das classes e a criação dos métodos. Atualizar os métodos que tratam as
# opções do menu, para funcionarem com as classes modeladas.

# Importando as bibliotecas
import textwrap
from abc import ABC, abstractmethod
from datetime import datetime

# Listas globais para armazenar os clientes e contador global de contas
clientes = []
contador_contas = 0

# Classe Cliente para armazenar informações dos clientes e suas contas
class Cliente:
    def __init__(self, nome, endereco, cpf):
        self.nome = nome            # Nome do cliente
        self.endereco = endereco    # Endereço do cliente
        self.cpf = cpf              # CPF do cliente
        self.contas = []            # Lista de contas associadas ao cliente

    # Realiza uma transação (saque ou depósito) em uma conta específica
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    # Adiciona uma nova conta ao cliente
    def adicionar_conta(self, conta):
        self.contas.append(conta)

    # Lista todas as contas do cliente
    def listar_contas(self):
        for i, conta in enumerate(self.contas):
            print(f" Conta {conta.numero}")

    # Permite selecionar uma conta entre as contas cadastradas
    def selecionar_conta(self):
        if len(self.contas) > 0:
            self.listar_contas()  # Mostra as contas para o cliente escolher
            numero_conta = int(input("Selecione o número da conta: "))
            for conta in self.contas:
                if conta.numero == numero_conta:
                    return conta  # Retorna a conta selecionada
            print("Número da conta inválido.")
        else:
            print("Este cliente não possui contas.")
        return None

# Classe Pessoa_Fisica para representar um cliente com CPF e data de nascimento
class Pessoa_Fisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(nome, endereco, cpf)  # Chama o construtor da classe base Cliente
        self.data_nascimento = data_nascimento # Armazena a data de nascimento do cliente

# Classe Conta para representar uma conta bancária genérica
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0            # Saldo inicial da conta
        self._numero = numero      # Número da conta
        self._agencia = '0001'     # Agência padrão
        self._cliente = cliente    # Cliente associado à conta
        self._historico = Historico()  # Histórico de transações da conta

    # Método de classe para criar uma nova conta
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    # Propriedades da conta (saldo, número, agência, cliente, histórico)
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    # Método para realizar saque na conta
    def sacar(self, valor):
        if valor > self._saldo:
            print('\nOperação não completada! Você não tem saldo suficiente.')
        elif valor > 0:
            self._saldo -= valor  # Deduz o valor do saldo
            print('Saque realizado com sucesso!')
            return True
        else:
            print('Operação Inválida! O valor informado é inválido.')
        return False

    # Método para realizar depósito na conta
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor  # Adiciona o valor ao saldo
            print('Depósito concluído com sucesso!')
            return True
        else:
            print('Operação Inválida! O valor informado é inválido.')
            return False

# Classe Conta_corrente, herda de Conta, com funcionalidades específicas para contas correntes
class Conta_corrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)  # Chama o construtor da classe base Conta
        self.limite = limite               # Limite de saque
        self.limite_saques = limite_saques # Limite de número de saques diários

    # Sobrescreve o método sacar da classe base para implementar limite de saques
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__])
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print('\nOperação não realizada. O valor do saque excede o limite de R$ 500,00.')
        elif excedeu_saques:
            print('Operação não realizada. Você excedeu o limite de 3 saques diários.')
        else:
            return super().sacar(valor)  # Chama o método sacar da classe base
        return False

# Classe Historico para armazenar transações feitas na conta
class Historico:
    def __init__(self):
        self._transacoes = []  # Lista de transações

    @property
    def transacoes(self):
        return self._transacoes

    # Adiciona uma transação ao histórico
    def adicionar_transacao(self, transacao):
        self._transacoes.append({'tipo': transacao.__class__.__name__,
                                 'valor': transacao.valor,
                                 'data': datetime.now().strftime('%d-%m-%Y %H:%M:%S')})

# Classe abstrata para definir uma transação
class Transacao(ABC):

    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

# Classe Saque, herda de Transacao e implementa a lógica de saque
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)  # Realiza o saque na conta
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)  # Registra a transação no histórico

# Classe Deposito, herda de Transacao e implementa a lógica de depósito
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)  # Realiza o depósito na conta
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)  # Registra a transação no histórico

# Função para coletar o endereço do cliente
def coletar_endereco():
    print('Endereço completo:\n')
    logradouro = input('Rua/Avenida: ')
    num_casa = input('N°: ')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    sigla_estado = input('Sigla do Estado (ex: SP, RJ): ')
    return f'{logradouro}, {num_casa} - {bairro} - {cidade}/{sigla_estado}'

# Função para validar o CPF
def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido! Deve conter 11 dígitos numéricos.")
        return False
    return True

# Função para buscar um cliente na lista global de clientes
def buscar_cliente(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

# Função para criar um novo cliente
def criar_cliente():
    print("\n================ Criar Cliente ================\n")
    print('Digite o nome ou 0 para retornar ao Meu Principal\n')

    nome = input("Nome: ")

    if nome.lower() == '0':
        return

    cpf = input("CPF: ")

    # Verifica se o CPF já está cadastrado
    if buscar_cliente(cpf):
        print(f"Erro: Cliente com CPF {cpf} já está cadastrado.")
        return

    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
    endereco = coletar_endereco()

    if validar_cpf(cpf):
        cliente = Pessoa_Fisica(nome, data_nascimento, cpf, endereco)
        clientes.append(cliente)
        print(f"\nCliente {nome} criado com sucesso!")
    else:
        print("Erro ao criar cliente. CPF inválido.")

# Função para abrir uma conta corrente para um cliente existente
def abrir_conta_corrente():
    global contador_contas  # Utilizando a variável global de contador
    print("\n================ Abrir Conta Corrente ================\n")
    print('Digite o CPF ou 0 para retornar ao Meu Principal\n')

    cpf = input("Informe o CPF do titular: ")

    if cpf.lower() == '0':
        return

    cliente = buscar_cliente(cpf)
    if cliente:
        contador_contas += 1  # Simula um número de conta incremental
        conta = Conta_corrente(contador_contas, cliente)
        cliente.adicionar_conta(conta)
        print(f"\nConta Corrente {contador_contas} aberta com sucesso para {cliente.nome}.")
    else:
        print("Cliente não encontrado. Verifique o CPF.")

# Função para realizar um depósito em uma conta
def realizar_deposito():
    print("\n================ Realizar Depósito ================\n")
    print('Digite o CPF ou 0 para retornar ao Meu Principal\n')

    cpf = input("Informe o CPF do titular: ")

    if cpf.lower() == '0':
        return

    cliente = buscar_cliente(cpf)
    if cliente:
        valor = float(input("Informe o valor do depósito: "))

        # Se o cliente tiver apenas uma conta, deposita diretamente
        if len(cliente.contas) == 1:
            conta = cliente.contas[0]
        else:
            # Caso tenha mais de uma, solicita a escolha da conta
            conta = cliente.selecionar_conta()

        if conta:
            transacao = Deposito(valor)
            cliente.realizar_transacao(conta, transacao)
    else:
        print("Cliente não encontrado. Verifique o CPF.")

# Função para realizar um saque em uma conta
def realizar_saque():
    print("\n================ Realizar Saque ================\n")
    print('Digite o CPF ou 0 para retornar ao Meu Principal\n')

    cpf = input("Informe o CPF do titular: ")

    if cpf.lower() == '0':
        return

    cliente = buscar_cliente(cpf)
    if cliente:
        valor = float(input("Informe o valor do saque: "))

        # Se o cliente tiver apenas uma conta, saca diretamente
        if len(cliente.contas) == 1:
            conta = cliente.contas[0]
        else:
            # Caso tenha mais de uma, solicita a escolha da conta
            conta = cliente.selecionar_conta()

        if conta:
            transacao = Saque(valor)
            cliente.realizar_transacao(conta, transacao)
    else:
        print("Cliente não encontrado. Verifique o CPF.")

# Função para exibir o extrato de uma conta
def exibir_extrato():
    print("\n================ Exibir Extrato ================\n")
    print('Digite o CPF ou 0 para retornar ao Meu Principal\n')

    cpf = input("Informe o CPF do titular: ")

    if cpf.lower() == '0':
        return

    cliente = buscar_cliente(cpf)
    if cliente:
        # Se o cliente tiver apenas uma conta, usa essa conta
        if len(cliente.contas) == 1:
            conta = cliente.contas[0]
        else:
            # Caso tenha mais de uma, solicita a escolha da conta
            conta = cliente.selecionar_conta()

        if conta:
            print(f"\nExtrato da Conta {conta.numero}:\n")
            for transacao in conta.historico.transacoes:
                print(f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
            print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
    else:
        print("Cliente não encontrado.")

# Função para excluir uma conta corrente de um cliente
def excluir_conta_corrente():
    print("\n================ Excluir Conta Corrente ================\n")
    print('Digite o CPF ou 0 para retornar ao Meu Principal\n')

    cpf = input("Informe o CPF do titular: ")

    if cpf.lower() == '0':
        return

    cliente = buscar_cliente(cpf)
    if cliente:
        # Se o cliente tiver apenas uma conta, remove essa conta
        if len(cliente.contas) == 1:
            conta = cliente.contas[0]
        else:
            # Caso tenha mais de uma conta, solicita a escolha
            conta = cliente.selecionar_conta()

        if conta:
            cliente.contas.remove(conta)
            print(f"\nConta {conta.numero} removida com sucesso.")
        else:
            print("Nenhuma conta foi removida.")
    else:
        print("Cliente não encontrado.")

# Função principal do sistema de banco, apresenta o menu principal
def main():
    while True:
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
        opcao = input(textwrap.dedent(menu))

        if opcao == 'd':
            realizar_deposito()
        elif opcao == 's':
            realizar_saque()
        elif opcao == 'e':
            exibir_extrato()
        elif opcao == 'c':
            abrir_conta_corrente()
        elif opcao == 'n':
            criar_cliente()
        elif opcao == 'ec':
            excluir_conta_corrente()
        elif opcao == 'sa':
            print("Obrigado por utilizar o Banco ByteBank!")
            break
        else:
            print("Opção inválida, tente novamente.")

# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    main()
