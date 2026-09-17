
# Variaveis
cargo = input("Diga seu cargo: ").strip().lower()
hora = int(input("Diga o horario atual "))
chave = input("A chave está ativa? ").lower()

# Ele cria a lista de cargos
ListaCargo = ["operador", "supervisor"]
ListaHorario = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
# Ele vai verificar o operador na [list]
for elemento in ListaCargo:
    # Apos verificar ele vai entrar na porta permitida ou nao
    # O acesso deve ser concedido se:
    # ◆ A chave_emergencia estiver ativa (True), O usuário for "supervisor"
    
    if cargo == elemento:
         if( chave == "sim") or (cargo == "supervisor") or hora in ListaHorario:
             print("1") 
# ◆ Caso contrário, o sistema deve exibir "Acesso Bloqueado".
         else: 
             print("Acesso bloqueado")