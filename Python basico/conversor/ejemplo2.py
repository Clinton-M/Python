#conversor de monedas


#funciones / molde
def conversorDeMoneda(tipoDeMoneda, valorDolar):
    valor = float(input(f"ingrese la cantidad de {tipoDeMoneda}π€ a convertir: π"))
    valor /=valorDolar
    valor = round(valor, 2)
    print(f"""
    la cantidad de {tipoDeMoneda}π€ que ingresaste es: π²{valor}dolares 
    
            gracais por usar nuestra aplicacion π«

    """)

def conversorDeMonedaa(tipoDeMoneda, valorDolar ):
    valor2 = float(input(f"ingrese la cantidad de {tipoDeMoneda}π€ a convertir: π"))
    valor2 *= valorDolar
    valor2 = round(valor2, 2)
    print(f"""
    la cantidad de {tipoDeMoneda}π€ que ingresaste es: π²{valor2}soles 
      """)


dato = int(input("""
    BIENVENIDO AL CONVERSOR DE MONEDASπ΅πΈ

    1. Sole a dolar π²
    2. Dolar a soles π°
    3. Salir π
    Escoja un opcion: ππ

"""))


match dato:
    case 1:
        conversorDeMoneda('soles', 3.85)
    case 2:
        conversorDeMonedaa('dolar', 3.85)
    case 3:
        exit()
    case other:
        print("opcion no valida π‘πΏπΏ")

        


# if dato ==1:
#     moneda = float(input("ingrese la cantidad de soles a convertir: "))
#     moneda /= 3.85
#     moneda = round(moneda, 2)
#     print(f"tienes: {moneda} dolares")
    

# elif dato ==2:
#     moneda = float(input("ingrese la cantidad de dolares a convertir: "))
#     moneda *= 3.85
#     moneda = round(moneda, 2)
#     # print(f"{moneda} soles")
#     print("usted tiene: ", moneda, " soles")

# elif dato ==3:
#     print("Gracias por usar el conversor de monedas")
#     exit()

# else:
#     print("opcion no valida")
#     print("adios")
    