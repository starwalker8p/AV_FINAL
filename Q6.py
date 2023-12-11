positivos = 0
soma = 0
for valores in range(1,7):
    valor = float(input(f"digite o {valores} valor: "))
    if valor > 0:
        positivos += 1
        soma += valor
media = soma/positivos
print(f"{positivos} valores positivos")
print(f"{round(media,2)}")