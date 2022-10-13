#Enunciado: Hallar el cociente y el residuo (resto) 
# de dos números enteros.

def run():
    num1 = int(input("Ingrese el primeri numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    cociente = num1 // num2
    residuo = num1 % num2
    print("El cociente es: ", cociente)
    print("El residuo es: ", residuo)
  

if __name__ =='__main__':
    run()

