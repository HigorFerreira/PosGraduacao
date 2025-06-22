contador = 0

def incrementa(valor):
    contador += valor
    return contador

print(incrementa(5))
# Saída: 5 (esperado)
print(incrementa(2))
# Saída: 8 (esperado)

contador = 100
print(incrementa(5))
# Saída: 105 (inesperado)