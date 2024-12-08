import timeit
import random
from proyecto.Punto2 import subastasFuerzaBruta,subastas_dinamico,subastas_voraz

def generar_datos_subasta(num_ofertas, max_acciones=1000, max_precio=500, max_minimo=300, max_maximo=600):
    """
    Genera valores aleatorios para A, B y una lista de ofertas.
    
    Args:
        num_ofertas (int): Número de ofertas a generar.
        max_acciones (int): Máximo valor para A (cantidad de acciones disponibles).
        max_precio (int): Máximo precio para B y el precio de cada oferta.
        max_minimo (int): Máximo valor para el mínimo de acciones de cada oferta.
        max_maximo (int): Máximo valor para el máximo de acciones de cada oferta.
        
    Returns:
        A (int): Cantidad de acciones disponibles.
        B (int): Precio mínimo aceptable por acción.
        ofertas (list): Lista de ofertas en el formato (precio, mínimo, máximo).
    """
    A = random.randint(1, max_acciones)        # Cantidad total de acciones disponibles
    B = random.randint(1, max_precio)          # Precio mínimo aceptable por acción
    
    ofertas = []
    for _ in range(num_ofertas):
        precio = random.randint(1, max_precio)  # Precio de la oferta
        minimo = random.randint(1, max_minimo)  # Mínimo de acciones que la oferta puede aceptar
        maximo = random.randint(minimo, max_maximo)  # Máximo de acciones que la oferta puede aceptar
        ofertas.append((precio, minimo, maximo))
    
    return A, B, ofertas


def medir_tiempos_subasta(A, B, ofertas):
    # Tiempo para la solución de fuerza bruta
    tiempo_fuerza_bruta = timeit.timeit(
        stmt=lambda: subastasFuerzaBruta(A, B, ofertas),
        number=3
    )

    # Tiempo para la solución dinámica
    tiempo_dinamico = timeit.timeit(
        stmt=lambda: subastas_dinamico(A, B, ofertas),
        number=3
    )

    # Tiempo para la solución voraz
    tiempo_voraz = timeit.timeit(
        stmt=lambda: subastas_voraz(ofertas, A, B),
        number=3
    )

    # Mostrar los resultados de tiempo para cada función
    print(f"Para A = {A}, B = {B}, con {len(ofertas)} ofertas:")
    print(f"  Fuerza Bruta: {tiempo_fuerza_bruta:.6f} segundos")
    print(f"  Programación Dinámica: {tiempo_dinamico:.6f} segundos")
    print(f"  Algoritmo Voraz: {tiempo_voraz:.6f} segundos\n")



if __name__ == "__main__":
    for longitud in [2, 6, 12, 16]:
        A, B, ofertas = generar_datos_subasta(num_ofertas=longitud,max_precio=150*longitud)
        #print(f"A (acciones disponibles): {A}")
        #print(f"B (precio mínimo): {B}")
        #print("Ofertas generadas (precio, mínimo, máximo):")
        #for oferta in ofertas:
        #    print(oferta)   
        medir_tiempos_subasta( A, B, ofertas)