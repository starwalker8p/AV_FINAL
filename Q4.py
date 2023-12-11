#coleto o ddd do usuario
ddd = int(input("digite o ddd: "))
cidades = {61: "Brasilia",71: "Salvador",11: "Sao Paulo",21: "Rio de Janeiro",32: "Juiz de Fora",19: "Campinas",27: "Vitoria",
31: "Belo Horizonte"}
#verifico se o ddd existe e de qual estado ele é
if ddd in cidades:
    print(cidades[ddd])
else:
    print("DDD nao cadastrado")