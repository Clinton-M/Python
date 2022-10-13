def run():
    
#   nombre  = input("Ingrese su nombre: ")
  

#   for letra in nombre :
#     print(letra)

    # frase = input("Ingrese una frase: ")

    # for letra in frase:
    #     print(letra.upper())

    # for numeros in range(1,11):
    #     numeros = list(range(1,11))
    #     print(numeros[::-1])
    # for contador in range(101):
    #     if contador % 2 != 0:
    #         continue
    #     print("numero pares :",contador)

    # for i in range(0,11):
    #     print(i)
    #     if i == 5:
    #         break
    texto = input("Ingrese un texto: ")
    for letra in texto:
        if letra == "a":
            break
        print("se encontro: ", letra)

if __name__ == '__main__':
    run()