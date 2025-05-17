from vehiculo import Vehiculo, imprimir_datos_vehiculo

class Vehiculo:
    def __init__(self, tipo, color, peso, ruedas=4, es_electrico=False, capacidad_pasajeros=5):
        self.tipo = tipo  # 'auto', 'moto', 'camion'
        self.color = color
        self.peso = peso
        self.ruedas = ruedas
        self.es_electrico = es_electrico
        self.capacidad_pasajeros = capacidad_pasajeros
        self.estado = "nuevo"

    def calcular_costo(self):
        if self.tipo == 'auto':
            base = 15000
            extra = self.peso * 100
            if self.es_electrico:
                extra += 5000
        elif self.tipo == 'moto':
            base = 8000
            extra = self.peso * 50
            if self.es_electrico:
                extra += 3000
        elif self.tipo == 'camion':
            base = 45000
            extra = self.peso * 200
        else:
            base = 0
            extra = 0
        return base + extra

    def necesita_inspeccion(self):
        if self.tipo == 'auto' and self.peso > 2000:
            return True
        elif self.tipo == 'moto' and self.peso > 300:
            return True
        elif self.tipo == 'camion':
            return True
        else:
            return False

def imprimir_datos_vehiculo(vehiculo):
    print(f"Vehiculo tipo: {vehiculo.tipo}")
    print(f"Color: {vehiculo.color}")
    print(f"Peso: {vehiculo.peso} kg")
    print(f"Ruedas: {vehiculo.ruedas}")
    print(f"Eléctrico: {'Sí' if vehiculo.es_electrico else 'No'}")
    print(f"Capacidad: {vehiculo.capacidad_pasajeros} pasajeros")
    print(f"Costo: ${vehiculo.calcular_costo()}")
    print(f"Requiere inspección: {'Sí' if vehiculo.necesita_inspeccion() else 'No'}")
    print("-------------------------")

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
