contador = 0

def incrementa(original, valor):
    return original + valor


print(contador:=incrementa(contador, 5))
# Saída: 5 (esperado)
print(contador:=incrementa(contador, 2))
# Saída: 8 (esperado)

contador = 100
print(contador:=incrementa(contador, 5))
# Saída: 105 (esperado)