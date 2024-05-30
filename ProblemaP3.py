# Mariana Ortega - 202211233
# Paulina Arrazola - 202020631

import sys
import time

def pancake(l:list)->list:
    #crea la lista donde se van a guardar los flips que se deben hacer 
    flips = []
    #cantidad de panqueques en la pila
    n = len(l)
    #centinela que indica si ya la pila de panqueques esta ordenada 
    #organizada es donde para l = [n,n-1,n-2...1]
    organizada = False
    #se ejecutará el ciclo siempre y cuando siga desogornizada la lista
    while organizada == False:
        #busca el mayor elemento que no esté en su posición
        mayor_desorganizado = verificar_organizada(l)
        #si es cero, no hya, entonces ya está organizado y termina
        if mayor_desorganizado ==0: 
            organizada = True
        else:
            #ya se cual es el elemnto, pero debo buscar donde está para hacer ahí el 1° flip
            pos_mayor_desorganzido = buscar(l, mayor_desorganizado)
            if pos_mayor_desorganzido == -1:
                l= flip_arriba_a_correcto(l)   
                flips.append(-mayor_desorganizado%n)
            else:
                flips.append(pos_mayor_desorganzido%n)
                l = flip_mayor_arriba(l, pos_mayor_desorganzido)
                flips.append(-mayor_desorganizado%n)
                l = flip_arriba_a_correcto(l)
    
    return flips,l
        

        
def verificar_organizada(l:list)->int:
    n = len(l)
    i = 0
    organizado = True
    mayor_desor = 0
    #Asumo que la lista está ya organizada, y encuentro el mayor elemento que esté desorganizado
    
    #tomando en cuenta que la lista organizada quiere decir que está de la siguiente manera con estas posiciones

    # la lista :  [  n  ,  n-1  ,  n-2  , ... ,  1  ]
    #                |      |       |            |
    # las pos:      -n   -(n-1)  -(n-2)         -1
    # por eso el ciclo, la variable a va de izquierda a derecha (0<=i<n) así
    # las pos:     -n+0   -n+1    -n+2        -n+(n-1)


    while i < n and organizado == True:
        #la estoy recorriendo de izquierda a derecha tomando las posiciones desde -n hasta -1
        #entonces a va de -n a -1 en el peor de los casos 
        a = -n + i
        #La explicación de arriba, el mayor desordenado sería el primero que no cumpla la condición 
        #que en la posición a debe estar el panqueque con valor = |a|
        #por ejemplo: a = -5+0, l[a]
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
        #este es el mismo a de antes, pero inicia desde el elemento desorganizado
        #porque no es necesario buscarlo desde el inicio de la lista, porque esas
        #posiciones ya están organizadas
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
        #voy sacando del final hasta la posicion del valor desorganizado, y metiendo a flipeada
        #esto para que se agreguen al contrario del orden en el que están
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
    
    #voy sacando del final hasta la posicion del valor desorganizado, y metiendo a flipeada
    #esto para que se agreguen al contrario del orden en el que están, y ya quedaría el mayor desorganizado organizado 
    for i in range(1, mayor_desorganizado+1) :
        valor = l[-i]
        organizada.append(valor)
        
    return organizada
    


def procesar_casos(archivo_entrada, archivo_salida):
    tiempo_ahora = time.time()
    with open(archivo_entrada, 'r') as f:
        numero_casos = int(f.readline().strip())
        resultados = []
        for __ in range(numero_casos):
            case_list = list(map(int, f.readline().strip().split()))
            flips, lista_org = pancake(case_list)
            if len(flips) == 0:
                resultados.append("ORDENADO")
            else:
                cadena = ' '.join(map(str, flips))
                resultados.append(f"{cadena}")

            if time.time() - tiempo_ahora > 150:
                break
    
    with open(archivo_salida, 'w') as f:
        for resultado in resultados:
            f.write(f"{resultado}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <archivo_entrada> <archivo_salida>")
    else:
        archivo_entrada = sys.argv[1]
        archivo_salida = sys.argv[2]
        procesar_casos(archivo_entrada, archivo_salida)

