def subastas_voraz(ofertas, A, B):
    # Ordenar ofertas por precio descendente
    ofertas_ordenadas = sorted(ofertas, key=lambda x: -x[0])
    cantidad_acciones = A
    compra_por_oferta = []

    # Recorrer las ofertas ordenadas
    for precio, minimo, maximo in ofertas_ordenadas:
        # Saltar ofertas con precio menor a B o si no se puede cumplir el mínimo
        if precio < B or minimo > cantidad_acciones:
            continue

        # Tomar la cantidad máxima posible para esta oferta
        acciones_tomadas = min(maximo, cantidad_acciones)
        compra_por_oferta.append(acciones_tomadas)
        cantidad_acciones -= acciones_tomadas

        # Terminar si ya no quedan acciones por asignar
        if cantidad_acciones == 0:
            break

    # Calcular ganancia máxima
    ganancia_maxima = sum(precio * acciones for (precio, _, _), acciones in zip(ofertas_ordenadas, compra_por_oferta))
    solucion = [f"Asignar {acciones} acciones a {precio}" for (precio, _, _), acciones in zip(ofertas_ordenadas, compra_por_oferta)]

    return ganancia_maxima, solucion

if __name__ == "__main__":
    # Definimos las ofertas en el formato (precio, mínimo, máximo)
    ofertas = [
        #(140, 200, 800), 
        (200, 300, 500),  
        (150, 200, 300),# 300 :v
        (50, 0 , 9000)

    ]

    A = 900  # Cantidad de acciones disponibles
    B = 50  # Precio mínimo aceptable por acción
    
    max_value, solucion_paso_paso = subastas_dinamico(A, B, ofertas)

    # Imprimimos los resultados
    print("Valor máximo recibido dinamico:", max_value)
    print("Paso a paso para llegar a la mejor solución:")
    for paso in solucion_paso_paso:
        print(paso)

    # Llamada al algoritmo
    resultado_final, paso_a_paso = subastas_voraz(ofertas, A, B)

    print(f"Valor máximo recibido voraz:", resultado_final)
    print("Las mejores ofertas y la cantidad de acciones asignadas son:")
    for paso in paso_a_paso:
        print(paso)