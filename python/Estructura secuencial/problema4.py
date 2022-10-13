#Enunciado: Hallar la potencia de a",
#  donde <<a>> y <<n» pertenecen a z• (números enteros positivos).


def run():
    a = int(input("Ingrese el numero a elevar: "))
    n = int(input("Ingrese el numero n: "))
    potencia = a ** n
    print("La potencia es: ", potencia)


if __name__ =='__main__':
    run()