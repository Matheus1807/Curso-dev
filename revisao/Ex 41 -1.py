# 1. Em um sistema escolar, as notas dos alunos precisam ser confiáveis.
# i. Uma nota nunca pode ser menor que 0.0 e nunca pode ser maior que 10.0.
# ii. Se deixarmos o atributo livre e público, qualquer linha de código externa poderia
# atribuir por engano valores absurdos como -5 ou 150.
# iii. Na próxima página encontram-se as restrições/passo-a-passo.

class Aluno:

    def __init__(self, nome="", nota=0.0):
        self.nome = nome
        self._nota = 0.0      # Atributo privado padrão
        self.nota = nota      # Usa o setter para validar a nota inicial
        self.situacao = 'Em análise'

    @property
    def nota(self):

        return self._nota

    @nota.setter
    def nota(self, nova_nota):
 
        try:
            valor = float(nova_nota)
            if 0 <= valor <= 10:
                self._nota = valor
            else:
                print(f"Erro: A nota {valor} é inválida! Deve estar entre 0.0 e 10.0.")
        except ValueError:
            print("Erro: O valor da nota deve ser um número.")

    def cadastro_interativo(self):
    
        self.nome = input('Digite o nome do aluno: ').strip().title()
        
        nota_input = input('Digite a nota do aluno (0 a 10): ')
        
        self.nota = nota_input  # Dispara a validação automática do @nota.setter


# --- Teste de Execução ---

# 1. Instanciando o objeto
aluno = Aluno()

# 2. Cadastro interativo via terminal
aluno.cadastro_interativo()

# 3. Testando atribuição direta válida e inválida
print("\n--- Testando atribuições diretas ---")
aluno.nota = 8.5   # Válido
print(f"Nota atual: {aluno.nota}")

aluno.nota = 150.0 # Inválido (exibe erro e mantém 8.5)
aluno.nota = -5.0  # Inválido (exibe erro e mantém 8.5)

print(f"Nome do Aluno: {aluno.nome}")
print(f"Nota Final Guardada: {aluno.nota}")