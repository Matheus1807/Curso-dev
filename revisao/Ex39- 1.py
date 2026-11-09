from datetime import datetime 

def registrar_evento(usuario, acao, status):

    with open('auditoria_sistema.log', 'a', encoding='utf-8') as arquivo:

        # Cabeçalho e separador
        arquivo.write(f'{"USUARIO":<15} | {"ACAO":<20} | {"STATUS":<10} | {'HORA':<10}\n')
        arquivo.write('-' * 53 + '\n')

        data_formatada = datetime.now().strftime('%d/%m/%Y; %H:%M:%S')
        # Registro do evento
        arquivo.write(f'{usuario:<15} | {acao:<20} | {status:<10} | {data_formatada} \n')

registrar_evento('eu', 'saque', 'sucesso')