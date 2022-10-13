#Dados 3 números, devolver los números en orden ascendente.

def run():
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    num3 = int(input("Ingrese otro número: "))
    

    if num1 > num2 and num1 > num3:
        numero_mayor = num1
    elif num2 > num1 and num2 > num3:
        numero_mayor = num2
    else:numero_mayor = num3

    if num1 < num2 and num1 < num3:
        numero_menor = num1
    elif num2 < num1 and num2 < num3:
        numero_menor = num2
    else:numero_menor = num3

    inter = (num1+num2+num3)-(numero_mayor+numero_menor)
    
    


    print(f"El mayor es: {numero_mayor}")
    print( f"El intermedio es: {inter}")
    print( f"El menor es: {numero_menor}")


if __name__ == "__main__":  
    run()