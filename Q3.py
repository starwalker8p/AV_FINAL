senha = 2002
#coleto a senha que o usuario ira inserir
senha_u = int(input("Digite a senha: "))
#verifico se é a correta
if senha_u == senha:
    print("Acesso Permitido")
else:
    print("Senha Invalida")
