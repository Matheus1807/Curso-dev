banco_dados = []
emailCorretos = ['@gmail.com', '@outlook.com']

#  coleta e armazenamento de dados de 5
for i in range(2):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    telefone = int(input('Digite seu telefone: '))
    email = input('Digite seu email: ')
    formacao = input('Digite sua formação: ')

# Verifica se o gmail foi digitado corretamente
    while not any(email.lower().endswith(dominio) for dominio in emailCorretos):
        print('Email errado!')
        email = input('Digite seu email: ')

# Candidatos com idade inferior a 18 anos não podem participar do processo.
    if idade < 18:
# exibir uma mensagem de recusa e tire do programa
        print(f'Cadastro recusado!')
        continue

# Cada candidato deve ser representado por um dicionário com os campos:
# "nome", "idade", "telefone", "email" e "formacao"
    cadastro = { 
    'nome': nome,
    'idade': idade,
    'telefone' : telefone,
    'email': email,
    'formacao' : formacao
}

# Todos os candidatos aprovados na triagem devem ser armazenados em uma
# lista principal chamada banco_candidatos.
    banco_dados.append(cadastro)

# Exibir um relatório contendo: Nome, E-mail e Formação
# de cada candidato apto.

for candito in banco_dados:
    print(candito['nome'], '\t', candito['email'], '\t', candito['formacao'])

# for i in range(len(banco_dados)):
#     print(f' Nome - {banco_dados[i]['nome']} | Email - {banco_dados[i]['email']} | Formação - {banco_dados[i] ['formacao']}')