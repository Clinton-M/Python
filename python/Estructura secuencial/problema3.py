#Enunciado: Dado el valor de venta de un producto,
#  hallar eiiGV (19 %) y el precio de venta.

def run():
    
    valor_venta = float(input("Ingrese el valor de venta del producto: "))
    gv = valor_venta * 0.19
    precio_venta = valor_venta + gv
    print("El Igv es: ", gv)
    print("El precio de venta es: ", precio_venta)

    
    

if __name__ =='__main__':
    run()