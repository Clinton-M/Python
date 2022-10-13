#Enunciado: Crear un programa para encontrar el
#  área de un círculo, use la fórmula :
#  area = π * r^2


import math

def run():
    radio = int(input("Ingrese el radio del círculo: "))
    area = math.pi * radio ** 2
    print("El área del círculo es: ", area)


if __name__ =='__main__':
    run()