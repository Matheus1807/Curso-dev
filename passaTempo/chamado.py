# Você precisa desenvolver um programa para registrar 
# e gerenciar esses atendimentos.
# Como e gerenciamento, tem q sair em uma hora
permitidosAdm = {
    "matheus": "1234",
    "admin": "4321"
}
usuarios = {
    "fran": "123",
    "julio": "1234",
    "tupac": "12345",
    "julia": "123456"
}

chamados = []
    # Loop responsável pela autenticação
while True:

    # Vê se você quer ficar no atendimento
    deseja_continuar = input(
        'Deseja continuar da central de atendimento?'
        ).lower().strip()

    if (
        deseja_continuar == 'nao') or (
            deseja_continuar == 'n') or (
                deseja_continuar == 'não'):
        break

    # Ele pega o login
    login = input("Digite seu usuário: ").lower().strip()
    senha = input("Digite sua senha: ").strip()
    
    # Verifica se você é admin do painel
    if login in permitidosAdm and permitidosAdm[login] == senha:
        
        print('-'*20)
        print("Acesso ao gerenciamento permitido!")
        print('-'*20)

        # Aqui ele printa todos os chamados
        print(f'{"ID":<5} {"NOME":<15} {"DESCRIÇÃO":<40} {"PRIORIDADE":<15} {"STATUS":<15}')
        print("-" * 80)

        for chamado in chamados:
            print(
                f'{chamado["id"]:<5} '
                f'{chamado["nome"]:<15} '
                f'{chamado["descricao"]:<40} '
                f'{chamado["prioridade"]:<15}'
                f'{chamado["status"]:<15}'
            )

        # Aqui ele busca um id especifico, se quiser
        busca_id = input(
            "Deseja buscar um id especifico? "
        ).lower().strip()

        # Se for sim ele busca
        if busca_id == "sim" or busca_id == "s":
            idenc = int(input("Diga um id: "))
            for chamado in chamados:
                if chamado["id"] == idenc:
                    print('Chamado encontrado!')
                    print(chamado['nome'] ['descricao'] ['prioridade'] ['status'])
                    break
            
        # Aqui ele pergunta se quer finalizar o genreciamento
        deseja_sair = input(
            "Deseja finalizar o gerenciamento? "
        ).lower().strip()

        if deseja_sair == "sim" or deseja_sair == "s":
            break


    # Se for apenas um cliente ele já 
    # te joga para o atendimento
    elif login in usuarios and usuarios[login] == senha:
        print('-'*20)
        print("Acesso ao gerenciamento permitido!")
        print('-'*20)

        while True:
            abrir_chamado = input(
                'Deseja abrir um chamado?'
            )

            if (abrir_chamado == 'sim') or (abrir_chamado == 's'):
                nome = input('Diga seu nome')
                descrição = input('Diga a descrição')
                prioridade = input('Diga a prioridade')
                id = len(chamados)+1

                novo_chamado = {
                    'nome': nome,
                    'descricao': descrição,
                    'prioridade': prioridade,
                    'id':id,
                    'status':'em aberto!'
                } 
                print("Chamado cadastrado!")
                chamados.append(novo_chamado)

            else:
                    print('Chamado finalizado!')
                    break
    else:
        print("Login ou senha incorretos!")
# break
        # Executado depois que o login for validado

print("Sistema encerrado!")