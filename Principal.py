import Funciones

lista=[1,4,6,12,14,31,44,2,17,8,99]

def main():
    while True:
        num = Funciones.solicitarValor(lista)
        encontrado = Funciones.busquedaSecuencial(lista, num)
        if encontrado == True:
            print("El valor ha sido encontrado en la lista...")
            break
        else:
            print("El valor no se encuentra en la lista")
main()