positivos = 0
soma = 0
#coleto os numeros e verificos se eles são positivos
for valores in range(1,7):
    valor = float(input(f"digite o {valores} valor: "))
    if valor > 0:
        positivos += 1
        soma += valor
#faço a media e exibo o resultado
media = soma/positivos
print(f"{positivos} valores positivos")
print(f"{round(media,2)}")