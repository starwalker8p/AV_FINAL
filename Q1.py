renda = 0
while renda <= 0:
    renda = float(input("Digite sua renda mensal: "))
impostos,rendas = [8, 18, 28],[2000,3000,4500]
if renda <= rendas[0]:
    print('Isento')
elif rendas[1] >= renda > rendas[0]:
    print(f"R$ {round(renda/100*impostos[0],2)}")
elif rendas[2] >= renda > rendas[1]:
    print(f"R$ {round(renda/100*impostos[1],2)}")
else:
    print(f"R$ {round(renda/100*impostos[2],2)}")