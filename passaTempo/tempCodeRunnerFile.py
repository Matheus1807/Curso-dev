        if busca_id == "sim" or busca_id == "s":
            idenc = int(input("Diga um id: "))
            if idenc in chamados:
                indice = chamados.index(idenc)
                print(f'{indice+1}')
            