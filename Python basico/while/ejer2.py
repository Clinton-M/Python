def run():
    print("potencia de 2")

    LIMITE = 100    
    contador = 0
    potencia_de_2  = 2**contador
    while potencia_de_2 < LIMITE:
        print("2 elevado a" + str(contador) + "es: " + str(potencia_de_2))
        contador += 1
        potencia_de_2 = 2**contador
        





if __name__ =='__main__':
    run()