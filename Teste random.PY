senha = "123"
login = input("Escolha uma senha: ")
while login != senha:
    print("Senha errada")
    login = input("Digite novamente: ")
print("Senha correta")