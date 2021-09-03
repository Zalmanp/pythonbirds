time = input("Que horas são: ")
if time.isdigit():
    time = int(time)
    if time < 0.00 or time > 23.:
        print("Horário deve estar entre 0 e 23")
    else:
        if time <= 12:
            print("Bom dia. ")
        elif time <= 17:
            print("Boa Tarde.")
        else:
            print("Boa Noite")
else:
    print("Digite um horario entre 0 e 23. ")
