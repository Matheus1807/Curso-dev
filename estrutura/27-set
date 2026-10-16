# Um formulário web recebeu múltiplos cadastros com e-mails repetidos: 
pythonemails_brutos = [
"ana@empresa.com", "carlos@provedor.com", "ana@empresa.com",
"beatriz@servico.com", "carlos@provedor.com", "daniel@tech.com"
]

# Converta a lista emails_brutos em um conjunto (set) chamado emails_unicos para 
# eliminar as redundâncias.   
emails_unicos = set(pythonemails_brutos)
print(emails_unicos)
# emails = list(emails_unicos) # vida real, tirou duplicatas, vira lista de novo

# Adicione um novo e-mail "marcos@tech.com" ao conjunto.
emails_unicos.add('marcos@tech.com') # isso seria o append da lista

# Verifique, por meio de um teste lógico (in), se o e-mail "carlos@provedor.com" 
# consta no conjunto e exiba uma mensagem informativa no terminal. 
print('carlos@provedor.com' in emails_unicos)  

# Exiba a quantidade total de e-mails válidos e únicos registrados.
print(len(emails_unicos))