# Uma rota administrativa da API exige o seguinte conjunto de permissões para ser
# executada:
permissoes_rota = {"AUTH_READ", "AUTH_WRITE", "DB_ADMIN", "LOG_EXPORT"}
# O sistema recuperou as permissões atribuídas a dois perfis de usuários distintos:
usuario_analista = {"AUTH_READ", "LOG_EXPORT"}
usuario_techlead = {"AUTH_READ", "AUTH_WRITE", "DB_ADMIN","LOG_EXPORT"\
                    , "BILLING_ACCESS"}

# 1. Identifique se cada um dos usuários tem acesso permitido à rota (todas as
# permissões de permissoes_rota devem estar contidas no conjunto do
# usuário)

for usuario in [usuario_analista, usuario_techlead]:
    if usuario_analista.issuperset(permissoes_rota):
        print(f'{usuario} acesso permitido.')

# Para o usuário que não tiver acesso, calcule e exiba via diferença entre
# conjuntos (difference ou operador -) exatamente quais permissões estão
# faltando para liberar o acesso.   