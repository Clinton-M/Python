#conversor de monedas


#funciones / molde
def conversorDeMoneda(tipoDeMoneda, valorDolar):
    valor = float(input(f"ingrese la cantidad de {tipoDeMoneda}🤑 a convertir: 🎒"))
    valor /=valorDolar
    valor = round(valor, 2)
    print(f"""
    la cantidad de {tipoDeMoneda}🤑 que ingresaste es: 💲{valor}dolares 
    
            gracais por usar nuestra aplicacion 🫂

    """)

def conversorDeMonedaa(tipoDeMoneda, valorDolar ):
    valor2 = float(input(f"ingrese la cantidad de {tipoDeMoneda}🤑 a convertir: 🎒"))
    valor2 *= valorDolar
    valor2 = round(valor2, 2)
    print(f"""
    la cantidad de {tipoDeMoneda}🤑 que ingresaste es: 💲{valor2}soles 
      """)


dato = int(input("""
    BIENVENIDO AL CONVERSOR DE MONEDAS💵💸

    1. Sole a dolar 💲
    2. Dolar a soles 💰
    3. Salir 🔐
    Escoja un opcion: 🙏😌

"""))


match dato:
    case 1:
        conversorDeMoneda('soles', 3.85)
    case 2:
        conversorDeMonedaa('dolar', 3.85)
    case 3:
        exit()
    case other:
        print("opcion no valida 😡👿👿")

        


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
    