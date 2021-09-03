num = input('Digite um número inteiro: ')
if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(f"{num} é par. ")
    else:
        print(f"{num} é impar. ")
else:
    print(f"{num} não é um numero inteiro. ")
