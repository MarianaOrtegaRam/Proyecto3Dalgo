import sys
import time

def pancake(l:list)->list:
    flips = []
    n = len(l)
    organizada = False
    while organizada == False:
        mayor_desorganizado = verificar_organizada(l)
        if mayor_desorganizado ==0: 
            organizada = True
        else:
            pos_mayor_desorganzido = buscar(l, mayor_desorganizado)
            if pos_mayor_desorganzido == -1:
                l= flip_arriba_a_correcto(l)   
                flips.append(-mayor_desorganizado%n)
            else:
                flips.append(pos_mayor_desorganzido%n)
                l = flip_mayor_arriba(l, pos_mayor_desorganzido)
                flips.append(-mayor_desorganizado%n)
                l = flip_arriba_a_correcto(l)
    
    return flips 
        
        
def verificar_organizada(l:list)->int:
    n = len(l)
    i = 0
    organizado = True
    mayor_desor = 0
    while i < n and organizado == True:
        a = -n + i
        if l[a] != abs(a):
            mayor_desor = abs(a)
            organizado = False
        i+=1
            
    return mayor_desor

def buscar(l:list, desorganizado:int) ->int:
    pos = 0
    i = 0
    encontrado = False
    while i < desorganizado and encontrado == False:
        a = -desorganizado+i
        valor = l[a]
        #print(a)
        #print(valor)
        #print("___________")
        if l[-desorganizado+i] == desorganizado:
            pos = -desorganizado + i
            encontrado = True
        i+=1
    
    return pos

def flip_mayor_arriba(l: list, pos: int)->list:
    
    """
    Parameters
    ----------
    l : list
        Lista que representa como están los pancakes actualmente.
    pos : int
        es la posición en donde está el mayor pancake que no está organizado
            está en valor negativo, por ejemplo:
         
        si la lista está así:
            [ 6 , 5 , 2 , 4 , 3 , 1]
             -6  -5  -4  -3  -2  -1
             
             la pos donde está el mayor elemento desorganizado es -3.

    Returns
    -------
    list
        la lista habiendo realizado el flip.

    """
    
    #A la lista orginal, se toman solo los elementos donde no se hará el flip
    #Es decir, de [ 6 , 5 , 2 , 4 , 3 , 1], flipeada es [ 6 , 5 , 2 ]
    
    flipeada = l[-len(l):pos]
    for i in range(1, abs(pos)+1) :
        valor = l[-i]
        flipeada.append(valor)
    return flipeada

def flip_arriba_a_correcto(l:list)->list:
    """

    Parameters
    ----------
    l : list
        Lista que representa como están los pancakes actualmente.
        
    Returns
    -------
    list
        La lista ya haciendo el flip correcto para que quede organizado.
    """
    
    #aca ya consideramos que el mayor desorganizado está en el tope (ultima pos)
    #por ejemplo l está así:  [6, 5, 2, 1, 3, 4], mayor_desorganizado es 4
    mayor_desorganizado = l[-1]
    
    
    #quiere decir que está organizado desde el inicio de la lista, hasta donde debería estár
    #el mayor desorganizado, es decir en la posicion -mayor_desorganizado
    #por ejemplo l está así:  [6, 5, 2, 1, 3, 4], organizada es  [6, 5]
    organizada = l[-len(l):-mayor_desorganizado]
    
    for i in range(1, mayor_desorganizado+1) :
        valor = l[-i]
        organizada.append(valor)
        
    return organizada
    


def procesar_casos(archivo):
    tiempo_ahora = time.time()
    with open(archivo, 'r') as f:
        numero_casos = int(f.readline().strip())
        for __ in range(numero_casos):
            case_list = list(map(int, f.readline().strip().split()))
            flips = pancake(case_list)
            if len(flips) == 0:
                print("ORDENADO")
            else:
                cadena = ' '.join(map(str, flips))
                print(cadena)

            if time.time() - tiempo_ahora > 150:
                break
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <archivo_entrada>")
    else:
        archivo_entrada = sys.argv[1]
        procesar_casos(archivo_entrada)

