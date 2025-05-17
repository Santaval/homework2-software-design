PRECIOS_BASE = {
    'auto': 15000,
    'moto': 8000,
    'camion': 45000
}
MULTIPLICADORES_PESO = {
    'auto': 100,
    'moto': 50,
    'camion': 200
}
EXTRA_ELECTRICO = {
    'auto': 5000,
    'moto': 3000,
    'camion': 0
}

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
        base = PRECIOS_BASE.get(self.tipo, 0)
        extra = self.peso * MULTIPLICADORES_PESO.get(self.tipo, 0)
        if self.es_electrico:
            extra += EXTRA_ELECTRICO.get(self.tipo, 0)
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