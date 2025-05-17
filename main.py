from vehiculo import Vehiculo, imprimir_datos_vehiculo

class Flota:
    def __init__(self):
        self.vehiculos = []

    def leer_datos_vehiculo(self):
        tipo = input("Tipo (auto/moto/camión): ").lower()
        color = input("Color: ")
        peso = float(input("Peso (kg): "))
        if tipo == 'moto':
            ruedas = 2
            capacidad = 2
        else:
            ruedas = 4
            capacidad = 5 if tipo == 'auto' else 2
        electrico = input("Es eléctrico? (s/n): ").lower() == 's'
        return tipo, color, peso, ruedas, electrico, capacidad

    def agregar_vehiculo(self):
        tipo, color, peso, ruedas, electrico, capacidad = self.leer_datos_vehiculo()
        v = Vehiculo(tipo, color, peso, ruedas, electrico, capacidad)
        self.vehiculos.append(v)
        print("Vehículo agregado!")

    def generar_reporte(self):
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
