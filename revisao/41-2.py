
class Produto:

    def __init__(self, nome="", preco=0, estoque=0):
        self.nome = nome
        self._preco = preco
        self._estoque = estoque

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):

        try:

            if novo_preco > 0:
                self._preco = novo_preco
                return True

            else:
                return False 

        except ValueError:
            print(
                "Erro: O novo preço deve ser um número.")

    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, novo_estoque):
        try:
            # CORREÇÃO: >= 0 para permitir que o estoque fique vazio (zero)
            if novo_estoque >= 0:
                self._estoque = novo_estoque
                return True
            else:
                # CORREÇÃO: Mensagem arrumada para estoque em vez de preço
                print('O estoque não pode ser negativo.')
                return False 
        except ValueError:
            print("Erro: O novo estoque deve ser um número e maior ou igual a 0.")

    def atualizar_dados(self):

        trocar_nome = input(
            'Diga o novo nome do produto (Deixe em branco para não alterar): '
            ).lower()

        if trocar_nome:
            self.nome = trocar_nome

        try:

            n_preco = float(
                input('Diga o novo preço do produto: '
                      ))
            self.preco = n_preco

            p_estoque = input('Teve alguma venda? (sim ou nao)').lower().strip()
            
            if p_estoque == ('sim') or p_estoque == ('s'):
                
                venda = int(
                    input('Diga quantas teve: '
                ))

                if self.estoque < venda:
                    print(
                        'Não é possivel vender mais do que tem no estoque'
                        )
                    
                elif self.estoque >= venda:
                    self.estoque = self.estoque - venda
                    print(f'Venda realizada! Estoque atualizado para {self.estoque}.')

            print(
                'Dados alterados com sucesso!'
                )

        except ValueError:
            print(
                "Erro: O novo preço deve ser um número."
                )


produto = Produto('Celular', 10, 100)
produto.atualizar_dados()
print(produto.nome, produto.preco, produto.estoque)    