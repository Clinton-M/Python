#Enunciado: Hallar la radicación de !l[a ,
#  donde <<a» y «n>> pertenecen a z• (números enteros positivos).

def run():
    a = int(input("Ingrese el numero a elevar: "))
    n = int(input("Ingrese el numero n: "))
    radicacion = a ** (1/n)
    radicacion = int(radicacion)
    print("La radicacion es: ", radicacion)



if __name__ =='__main__':
    run()