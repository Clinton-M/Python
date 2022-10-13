
#conversor de monedas
# dolar a sol = 3.85
# sol a dolar = 1


def conversorDeMoneda(tipoDeMoneda, valorDolar):
    moneda = float(input("cuantas monedas en " + tipoDeMoneda + " " + "tienes?: "))
    moneda /=valorDolar
    moneda = round(moneda, 2)
    
    
    print("tienes $ " + str(moneda) +" " + tipoDeMoneda)
    print("gracias")

def convDolarSoles(tipoDeMoneda, valorDolar, valorSoles):
    monedaa = float(input("cuantas monedas en " + tipoDeMoneda + " " + "tienes?: "))
    monedaa *= valorDolar*valorSoles
    monedaa = round(monedaa, 2)

    print("tienes $ " + str(monedaa) +" " + tipoDeMoneda)
    

menu = """
vienvenido al conversor de monedas 😊

1. Convertir de soles a dolares
2. Convertir de pesos argentinos a dolares
3. Convertir de dolares a soles

elija una opcion: """

opcion = int(input(menu))


match opcion:
    case 1:
        conversorDeMoneda("soles", 3.85)
        
    case 2:
        conversorDeMoneda("angentino", 35)

    case 3:
        convDolarSoles("dolar", 1, 3.85)

    case other:
        print("opcion no valida")



