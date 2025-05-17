from vehiculo import crear_vehiculo

class Flota:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, tipo, color, peso, ruedas, electrico, capacidad):
        v = crear_vehiculo(tipo, color, peso, ruedas, electrico, capacidad)
        self.vehiculos.append(v)
        print("Vehículo agregado!")

    def generar_reporte(self):
        from vehiculo import imprimir_datos_vehiculo
        total = 0
        electricos = 0
        requiere_inspeccion = 0

        for v in self.vehiculos:
            imprimir_datos_vehiculo(v)
            total += v.calcular_costo()
            if v.es_electrico:
                electricos += 1
            if v.necesita_inspeccion():
                requiere_inspeccion += 1

        print(f"\nRESUMEN FLOTA:")
        print(f"Total vehículos: {len(self.vehiculos)}")
        print(f"Vehículos eléctricos: {electricos}")
        print(f"Requieren inspección: {requiere_inspeccion}")
        print(f"Valor total: ${total}") 