import random


def run():
    # numero_secreto = random.randint(1, 100)
    # while True:
    #     print("adivina el numero")
    #     numero = int(input("ingresa un numero: "))
    #     if numero == numero_secreto:
    #         print("ganaste")
    #         break
    #     else:
    #         print("perdiste")
    numero_secreto = random.randint(1,100)
    numero_elegido = int(input("ingresa un numero: "))
    while numero_elegido != numero_secreto:
        if numero_elegido < numero_secreto:
            print("el numero es mayor")
        else:
            print("el numero es menor")
        numero_elegido = int(input("ingresa un numero: "))
    print("ganaste")


if __name__ =='__main__':
    run()