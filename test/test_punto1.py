import timeit

# Generador de palabras aleatorias
import random
import string
from proyecto.Punto1 import Terminal

terminal_inteligente = Terminal()

def generar_palabra_aleatoria(longitud):
    """Genera una palabra aleatoria de la longitud especificada."""
    letras = string.ascii_lowercase  # Caracteres a usar: letras minúsculas
    return ''.join(random.choice(letras) for _ in range(longitud))

def medir_tiempos_terminal(longitud_palabra):
    cadena1 = generar_palabra_aleatoria(longitud_palabra)
    cadena2 = generar_palabra_aleatoria(longitud_palabra)
    #5 repeticiones para cada funcion a medir
    tiempo_fuerza_bruta = timeit.timeit(
        stmt=lambda: terminal_inteligente.terminal_fuerzaBruta(cadena1, cadena2),
        number=5
    )
    
    tiempo_dinamica = timeit.timeit(
        stmt=lambda: terminal_inteligente.terminal_dinamica(cadena1, cadena2),
        number=5
    )
    
    tiempo_voraz = timeit.timeit(
        stmt=lambda: terminal_inteligente.terminal_voraz(cadena1, cadena2),
        number=5
    )
    
    # Muestra los resultados
    print(f"Para palabras de longitud {longitud_palabra}:")
    print(f"  Fuerza Bruta: {tiempo_fuerza_bruta:.6f} segundos")
    print(f"  Programación Dinámica: {tiempo_dinamica:.6f} segundos")
    print(f"  Algoritmo Voraz: {tiempo_voraz:.6f} segundos\n")


if __name__ == "__main__":
    # Ejecutar pruebas para diferentes tamaños de palabra
    for longitud in [5, 10, 15, 20]:  
        medir_tiempos_terminal(longitud)

