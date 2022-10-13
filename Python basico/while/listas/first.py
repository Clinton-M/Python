dias_De_La_Semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

numero = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


dias_De_La_Semana.append("Domingo")
dias_De_La_Semana.pop(-1) # Elimina el ultimo elemento de la lista

for dia in dias_De_La_Semana:
    
    print(dia[::-1]) # Imprime el dia de la semana al reves

