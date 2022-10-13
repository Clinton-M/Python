#Enunciado: Dada una cantidad de horas, obtener su equivalente en minutos y segundos.

def run():
    horas = int(input("Ingrese la cantidad de horas: "))
    minutos = horas * 60
    segundos = minutos * 60
    
    print("La cantidad  es: ", minutos , "minutos: ", segundos)


if __name__ =='__main__':
    run()