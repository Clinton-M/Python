#Enunciado: Crear un programa que permita convertir
#  una cantidad de segundos en horas, minutos y 
#segundos.

def run():
    segundos = int(input("Ingrese la cantidad de segundos: "))

    horas = segundos // 3600
    segundos_restantes = segundos % 3600
    minutos = segundos_restantes // 60
    segundos_finales = segundos_restantes % 60



    print("La cantidad  es: ", horas , "minutos: ", minutos, "segundos: ", segundos_finales)
    


if __name__ =='__main__':
    run()