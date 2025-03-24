class SistemaTransporte:
    def __init__(self):
        self.rutas = {}  # Diccionario para almacenar las rutas y sus conexiones
        self.conocimiento = []  # Lista para almacenar las reglas lógicas

    #Métodos
    def agregar_ruta(self, origen, destino, tiempo, costo):
        """Agrega una nueva ruta al sistema."""
        if origen not in self.rutas:
            self.rutas[origen] = []
        self.rutas[origen].append({"destino": destino, "tiempo": tiempo, "costo": costo})

    def agregar_regla(self, regla):
        """Agrega una nueva regla lógica a la base de conocimiento."""
        self.conocimiento.append(regla)

    def encontrar_mejor_ruta(self, inicio, fin):
        """Encuentra la mejor ruta desde el punto de inicio hasta el punto final."""
       
        mejor_ruta = []
        mejor_tiempo = float('inf')
        mejor_costo = float('inf')

        def buscar_ruta(actual, ruta_actual, tiempo_actual, costo_actual):
            nonlocal mejor_ruta, mejor_tiempo, mejor_costo

            if actual == fin:
                if tiempo_actual < mejor_tiempo or (tiempo_actual == mejor_tiempo and costo_actual < mejor_costo):
                    mejor_ruta = ruta_actual[:]
                    mejor_tiempo = tiempo_actual
                    mejor_costo = costo_actual
                return

            if actual not in self.rutas:
                return

            for conexion in self.rutas[actual]:
                if conexion["destino"] not in ruta_actual:
                    nueva_ruta = ruta_actual + [conexion["destino"]]
                    nuevo_tiempo = tiempo_actual + conexion["tiempo"]
                    nuevo_costo = costo_actual + conexion["costo"]
                    buscar_ruta(conexion["destino"], nueva_ruta, nuevo_tiempo, nuevo_costo)

        buscar_ruta(inicio, [inicio], 0, 0)

        if mejor_ruta:
            return mejor_ruta, mejor_tiempo, mejor_costo
        else:
            return None, None, None

# Ejemplo de uso
sistema = SistemaTransporte()

# Agregando rutas (origen, destino, tiempo, costo)
sistema.agregar_ruta("A", "B", 10, 2.5)
sistema.agregar_ruta("B", "C", 15, 3.0)
sistema.agregar_ruta("A", "C", 25, 4.0)
sistema.agregar_ruta("C", "D", 10, 2.0)
sistema.agregar_ruta("A", "D", 45, 10.0)

# Agregar reglas 
sistema.agregar_regla("Si hay mucho tráfico en la ruta, aumentar el tiempo estimado.")
sistema.agregar_regla("Si es hora pico, aumentar el costo.")

inicio = "A"
fin = "D"

ruta, tiempo, costo = sistema.encontrar_mejor_ruta(inicio, fin)

if ruta:
    print(f"Mejor ruta: {ruta}")
    print(f"Tiempo estimado: {tiempo} minutos")
    print(f"Costo estimado: ${costo}")
else:
    print("No se encontró una ruta.")