# Entrada: s = "abcd", t = "abcde"
# Saída: "e"
# Explicação: 'e' é a letra que foi adicionada.
s = "abcd"
t = "abcde"

for letra in t:
    # Verifica se a letra atual não aparece em s.
    if letra not in s:
        print(f"A letra adicionada foi: {letra}")