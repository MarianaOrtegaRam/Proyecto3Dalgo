# Mariana Ortega - 202211233
# Paulina Arrazola - 202020631

import random


def generate_string(start, end):
    numbers = random.sample(range(start, end + 1), end - start + 1)
    numbers_str = ' '.join(map(str, numbers))
    return numbers_str

def numeros_faltantes(lista, inicio, fin):
    """
    Encuentra los números que faltan en una lista dentro de un rango dado.

    Parameters:
    lista (list): La lista de números.
    inicio (int): El número inicial del rango.
    fin (int): El número final del rango.

    Returns:
    list: Una lista de los números que faltan en el rango especificado.
    """
    # Crear un conjunto de todos los números en el rango especificado
    conjunto_completo = set(range(inicio, fin + 1))
    # Crear un conjunto de los números que están en la lista
    conjunto_lista = set(lista)
    # Encontrar la diferencia entre los dos conjuntos
    faltantes = conjunto_completo - conjunto_lista
    # Convertir el conjunto de faltantes a una lista y ordenarla
    return sorted(list(faltantes))


B = generate_string(1, 1000)
print(B)
