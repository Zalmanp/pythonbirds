nome = input("escreva seu nome: ")
qtd_carcteres = len(nome)
if qtd_carcteres <= 4:
    print("seu nome é curto")
elif qtd_carcteres <= 6:
    print("Seu nome é normal")
else:
    print("seu nome muito grande")
