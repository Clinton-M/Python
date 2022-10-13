def run():
    diccionario = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': '30'}
    # for key, value in diccionario.items(): #items() devuelve una tupla con las llaves y los valores
    #     print(key, value)

    for valores in diccionario.values(): #values() devuelve una tupla con los valores
        print(valores)

    for llaves in diccionario.keys(): #keys() devuelve una tupla con las llaves
        print(llaves)

    for llaves, valores in diccionario.items(): #items() devuelve una tupla con las llaves y los valores    
        print(llaves,": ", valores)
        

if __name__ == '__main__':
    run()