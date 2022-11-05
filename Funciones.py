def solicitarValor(lista):
    for val in lista:
        print(val, end=" , ")
    num = int(input("\nIngresa un valor: "))
    return num

def busquedaSecuencial(lista, num):
    for i in range(0,len(lista)):
        if num==lista[i]:
            return True
    return False
    