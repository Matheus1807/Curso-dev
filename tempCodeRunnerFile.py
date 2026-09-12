# Variaveis
numero1 = float(input("O primeiro lado "))
numero2 = float(input("O segundo lado "))
numero3 = float(input("O terceiro lado "))
# Soma dos lados
sn = numero1 + numero2
# Verifica se o sn > é maior que o terceiro lado
if sn > numero3:
    print("a soma dois lados é maior que o terceiro lado")

    # Verisifica se é Equilatero
    if (numero1 == numero2)\
        and (numero2 == numero3):
        print("Triangulo Equilátero")

    # Verisifica se é Isoceles

    elif (numero2 == numero1 != numero3)\
          or (numero1 == numero3 != numero2)\
          or (numero3 == numero2 != numero1 ):
        print("Triângulo isóceles")

    # Se não for nenhum dos dois, tem que ser Escaleno

    else:
        print("Escaleno")
else:
    print("""
[ERRO CRÍTICO DO SISTEMA]

Acesso não autorizado detectado.
Conexão externa estabelecida.
Tentativa de acesso aos arquivos do sistema em andamento...

IP: 192.168.0.*** 
Status: COMPROMETIDO
Código do erro: 0xA93F21

[AVISO: atividade suspeita detectada.
""")