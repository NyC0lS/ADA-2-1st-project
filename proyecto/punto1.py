class Terminal:
    def __init__(self, costo_insert=2, costo_delete=2, costo_replace=3, costo_kill=1, costo_advance=1):
        self.costo_insert = costo_insert
        self.costo_delete = costo_delete
        self.costo_replace = costo_replace
        self.costo_kill = costo_kill
        self.costo_advance = costo_advance

    def cambiar_costos(self, insert, delete, replace, kill, advance):
        self.costo_insert = insert
        self.costo_delete = delete
        self.costo_replace = replace
        self.costo_kill = kill
        self.costo_advance = advance

    def obtener_costos(self):
        return {
            "insert": self.costo_insert,
            "delete": self.costo_delete,
            "replace": self.costo_replace,
            "kill": self.costo_kill,
            "advance": self.costo_advance
        }
 
 def terminal_voraz(self, ca1, ca2):
        def terminal_voraz_aux(cadena1, cadena2, pasos, costo_total):
            if len(cadena1) == 0:
                costo = self.costo_insert * len(cadena2)
                return costo + costo_total, pasos + [f"insert {x}" for x in cadena2]
            
            if len(cadena2) == 0:
                if self.costo_delete * len(cadena1) < self.costo_kill:
                    return costo_total + (self.costo_delete * len(cadena1)), pasos + [f"delete {x}" for x in cadena1]
                else:
                    return costo_total + self.costo_kill, pasos + ["kill"]
            
            # Calcular los costos directos de cada operación
            beneficio_insertar = self.costo_insert
            beneficio_eliminar = self.costo_delete
            beneficio_reemplazar = self.costo_replace
            beneficio_avanzar = float("inf")
            
            if cadena1[0] == cadena2[0]:
                beneficio_avanzar = self.costo_advance

            # Crear lista de opciones con desempate basado en prioridad
            opciones = [
                (beneficio_avanzar, pasos + ["advance"], "avanzar"),
                (beneficio_reemplazar, pasos + [f"replace {cadena1[0]} with {cadena2[0]}"], "reemplazar"),
                (beneficio_insertar, pasos + [f"insert {cadena2[0]}"], "insertar"),
                (beneficio_eliminar, pasos + ["delete"], "eliminar")
            ]
            
            # Ordenar las opciones por costo y luego por prioridad
            opciones.sort(key=lambda x: (x[0], ["avanzar", "reemplazar", "insertar", "eliminar"].index(x[2])))

            # Seleccionar la mejor opción
            costo, nuevos_pasos, accion = opciones[0]

            if accion == "avanzar":
                return terminal_voraz_aux(cadena1[1:], cadena2[1:], nuevos_pasos, costo_total + self.costo_advance)
            elif accion == "reemplazar":
                return terminal_voraz_aux(cadena1[1:], cadena2[1:], nuevos_pasos, costo_total + self.costo_replace)
            elif accion == "insertar":
                return terminal_voraz_aux(cadena1, cadena2[1:], nuevos_pasos, costo_total + self.costo_insert)
            elif accion == "eliminar":
                return terminal_voraz_aux(cadena1[1:], cadena2, nuevos_pasos, costo_total + self.costo_delete)

        return terminal_voraz_aux(ca1, ca2, [], 0)


if __name__ == "__main__":
    cadena1 = "francesa"
    cadena2 = "ancestro"
    #5+2+3+8+1


    #print(terminal_fuerzaBruta(cadena1,cadena2))
    #print(terminal_dinamica(cadena1,cadena2))
    #print(terminal_voraz(cadena1,cadena2))