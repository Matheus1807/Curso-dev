class Conta:

    def __init__(self, nome, conta, saldo=0):
        self.nome = nome
        self.conta = conta
        self.saldo = saldo

    def realizar_deposito(self, valor):
        # verifica se o valor é positivo, entra caso não seja
        if valor <= 0:
            print('Digite um valor válido')
            return

        self.saldo += valor

    def realizar_saque(self, valor):
        if valor <= 0:
            print('Digite um valor válido')
            return
        if self.saldo < valor:
            print('Você não tem saldo suficiente')
            return

        # caso tudo de certo, faz o saque
        # self.saldo = self.saldo - valor
        self.saldo -= valor
        
    def realizar_transferencia(self, conta_destino, valor):
        self.realizar_saque(valor)
        conta_destino.realizar_deposito(valor)


conta_do_Valim = Conta('Valim', '00001', 20)
print(conta_do_Valim.saldo)
print(conta_do_Valim.nome)
        
class ContaPoupanca(Conta):

    def __init__(self, nome, conta, rendimento, saldo=0):
        super().__init__(nome, conta, saldo)
        self.rendimento = rendimento

# self // this

# class Carro:

#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

# c1 = Carro('Fiat', 'Palio', '2002')
# c2 = Carro('Ford', 'Fusion', '2014')