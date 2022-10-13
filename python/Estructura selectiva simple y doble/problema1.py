#Enunciado: Dado dos números enteros diferentes, devolver el número mayor.

def run():
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    if num1 > num2:
        print(f"El mayor es: {num1}")
    else:
        print(f"El mayor es: {num2}")




if __name__ == "__main__":
    run()




