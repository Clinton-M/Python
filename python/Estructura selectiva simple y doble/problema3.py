# Enunciado: Un restaurante ofrece un descuento del 10 % para consumos de hasta S/.100.00 y un 
# descuento de 20% para consumos mayores. Para ambos casos se aplica un impuesto del19 %. Determinar 
# el monto del descuento, el impuesto y el importe a pagar.

def run():
    monto = float(input("Ingrese el monto: "))
    if monto <= 100:
        descuento = monto * 0.1
    else:
        descuento = monto * 0.2

    impuesto = (monto - descuento) * 0.19
    importe = monto - descuento + impuesto
    
    print(f"El descuento es: {descuento}")
    print(f"El impuesto  IGV es: {impuesto}")
    print(f"El importe a pagar es: {importe}")

 
if __name__ == "__main__":
    run()