


# def imprimir_mensaje():
#     print("mesan especial")
#     print("mesan  lalalal")
    


# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def conversacion(mensaje): #funcion que recibe un parametro
    print("hola")
    print("como estas")
    print(mensaje)


opcion = int(input("elige una opcion(1; 2; 3):  "))

if opcion == 1:
   conversacion("elegiste opcion 1")

elif opcion == 2:
    conversacion("elegiste opcion 2")

elif opcion == 3:
     conversacion("elegiste opcion 3")

else:
    print("opcion no valida")