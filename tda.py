def creare_lista_int():
    lista_locala = []
    for i in range(n):
            n = int(input('Nr. de elemente = ?'))
            elem = int(input('Numarul intreg '+str(i)+' este:'))
            lista_locala.append(elem)
    return lista_locala
lista1=creare_lista_int()
print(lista1)

def creare_lista_str():
    lista_locala = []
    for i in range(n):
            n = int(input('Nr. de elemente = ?'))
            elem = str(input('Caracterul '+str(i)+' este:'))
            lista_locala.append(elem)
    return lista_locala
lista2=creare_lista_str()
print(lista2)
