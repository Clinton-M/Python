
def palindromo (palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabraInvertida = palabra[::-1]
    if palabra == palabraInvertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('La palabra es palindroma')
    else:
        print('La palabra no es palindroma')


if __name__ =='__main__':
    run()