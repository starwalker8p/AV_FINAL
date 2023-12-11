valores = []
pares = 0
for numeros in range(1,6):
    valor = int(input(f"digite o {numeros} valor: "))
    valores.append(valor)
    if valor % 2 == 0:
        pares += 1
print(f"{pares} valores pares")