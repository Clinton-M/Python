#Enunciado: Convertir grados sexagesimales a centesimales.

def run():
    grados = int(input("Ingrese la cantidad de grados: "))
    centesimales = grados * 100 / 60
    print("La cantidad  es: ", centesimales)


if __name__ =='__main__':
    run()