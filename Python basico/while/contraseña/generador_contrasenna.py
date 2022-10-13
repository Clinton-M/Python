import random

def regerate_password():
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
     'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special = ['!', '"', '#', '$', '%', '&', '/', '(', ')', '=', '?', '¿', '¡', '*', '+', '-', '.', ',']
   
    carater = upper+lower+numbers+special
    password =[]
    for i in range(10):
        password_ramdom =random.choice(carater) #random.choice(carater) eige ramdom caracter
        password.append(password_ramdom)

    password = ''.join(password) #concatena los caracteres
    return password


def run():
    password = regerate_password()
    # print('La contraseña generada es: {}'.format(password))
    print("tu contraseña es:"+password)


if __name__ == '__main__':
    run()