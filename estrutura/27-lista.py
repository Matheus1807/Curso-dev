# Inicialize uma lista chamada fila_tarefas contendo: 
# "Backup", "Envio de Logs", "Limpeza de Cache".
fila_tarefas = ['Backup', 'Envio de Logs', 'Limpeza de Cache']

# Adicione uma nova tarefa "Atualização de Dependências" ao final da lista.
fila_tarefas.append('Atualização de Dependências')

# Insira a tarefa de emergência "Correção de Bug Crítico" na primeira posição 
# (índice 0).
fila_tarefas.insert(0, 'Correção de Bug Crítico')

# Remova a tarefa concluída "Limpeza de Cache" pelo seu nome/valor.
fila_tarefas.remove('Limpeza de Cache')

# Imprima o total de tarefas restantes e exiba qual tarefa está no primeiro e 
# qual está no último índice da lista.
print(len(fila_tarefas))
print(fila_tarefas[0])
print(fila_tarefas[-1]) # outro jeito: fila_tarefas[len(fila_tarefa