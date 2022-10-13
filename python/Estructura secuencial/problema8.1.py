#Enunciado: Dado 4 números enteros, obtener el porcentaje de cada uno en función a la suma de los 4 
#números ingresados.

def run():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    num3 = int(input("Ingrese el tercer numero: "))
    num4 = int(input("Ingrese el cuarto numero: "))
    suma = num1 + num2 + num3 + num4
    porcentaje1 = num1 * 100 / suma
    porcentaje2 = num2 * 100 / suma
    porcentaje3 = num3 * 100 / suma
    porcentaje4 = num4 * 100 / suma
    print("El porcentaje del primer numero es: ", porcentaje1)
    print("El porcentaje del segundo numero es: ", porcentaje2)
    print("El porcentaje del tercer numero es: ", porcentaje3)
    print("El porcentaje del cuarto numero es: ", porcentaje4)

if __name__ =='__main__':
    run()