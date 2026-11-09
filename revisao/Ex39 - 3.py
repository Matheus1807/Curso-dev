with (open('emails_brutos.txt', "r", encoding='utf-8') as arquivo,
    open('emails_padronizados.txt.', "w") as arq_saida):

    for linha in arquivo:

        conteudo = linha.lower().strip()
        
        arq_saida.write(conteudo + "\n")