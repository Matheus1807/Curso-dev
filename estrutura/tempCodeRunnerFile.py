    if usuario_analista.issuperset(permissoes_rota):
        print(f'acesso permitido.')

# Para o usuário que não tiver acesso, calcule e exiba via diferença entre
# conjuntos (difference ou operador -) exatamente quais permissões estão
# faltando para liberar o acesso.