#coleto o salario
salario=0
while salario <= 0:
    salario = float(input("digite seu salario: "))
faixas = [(0, 400.00, 15),(400.01, 800.00, 12),(800.01, 1200.00, 10),(1200.01, 2000.00, 7),(2000.01, float('inf'), 4)]
nsalario = 0
p_r = 0
#dfaço o conta do novo salario
for faixa in faixas:
    if faixa[0]<=salario<=faixa[1]:
        p_r = faixa[2]
        nsalario = salario+(salario*p_r/100)
v_r = nsalario-salario
print(f'{round(nsalario,2)}')
print(f'{round(v_r,2)}')
print(f'{round(p_r,2)} %')
