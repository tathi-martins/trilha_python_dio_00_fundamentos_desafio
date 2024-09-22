# Desafios da Trilha Python Bootcamp NTT Data da Digital Innovation One

## Módulo I - Fundamentos
Criar um sistema de banco com as operações depositar, sacar e extrato. Desafio da trilha Python (Fundamentos) da plataforma DIO, para o bootcamp da NTT Data

### Requisitos do desafio:
Um sistema de banco simples com apenas três operações: depósito, saque e extrato. A versão 1 terá apenas um usuário. Não será necessário identificar os usuários, a agência e a conta bancária.

### Operação Depósito: 
Todos os depósito devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação Saque: 
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por saldo insuficiente. Todos os saques devem ser armazenadados em uma variável e exibidos na operação de extrato

### Operação de Extrato: 
Deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Os valores devem exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 -> R$ 1500.45

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Desafio 2:

## Módulo II - Coleções em Python

Precisamos deixar o nosso código mais modularizado, para isso, vamos criar funções para as operações existentes: sacar, depositar e visualizar histórico. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

## Requisitos do desafio:

### Operação Depósito: 
A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato

### Operação Saque: 
A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques. Sugestão de retorno: saldo e extrato.

### Operação de Extrato: 
A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo. Argumentos nomeados: extrato.

### Precisamos criar duas novas funções: 
Criar usuário e criar conta corrente. Fique a vontade para adicionar mais funções, exemplo, listar contas.

### Função criar usuário (cliente): 
Programa deve armazenar os usuários em uma lista, um usuário é composto por nome, data de nascimento, CPF e endereço. O endereço é uma string com formato; logradouro, n° - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF (deve ser string). Não podemos cadastrar 2 usuários com o mesmo CPF.

### Criar conta corrente: 
O programa deve armazenar contas em uma lista, uma conta é composta por agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

### Dica: 
Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.
