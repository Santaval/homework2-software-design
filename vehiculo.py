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
        self.tipo = tipo
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
        return False

class Auto(Vehiculo):
    def __init__(self, color, peso, ruedas=4, es_electrico=False, capacidad_pasajeros=5):
        super().__init__('auto', color, peso, ruedas, es_electrico, capacidad_pasajeros)
    def necesita_inspeccion(self):
        return self.peso > 2000

class Moto(Vehiculo):
    def __init__(self, color, peso, ruedas=2, es_electrico=False, capacidad_pasajeros=2):
        super().__init__('moto', color, peso, ruedas, es_electrico, capacidad_pasajeros)
    def necesita_inspeccion(self):
        return self.peso > 300

class Camion(Vehiculo):
    def __init__(self, color, peso, ruedas=4, es_electrico=False, capacidad_pasajeros=2):
        super().__init__('camion', color, peso, ruedas, es_electrico, capacidad_pasajeros)
    def necesita_inspeccion(self):
        return True

def crear_vehiculo(tipo, color, peso, ruedas, es_electrico, capacidad_pasajeros):
    if tipo == 'auto':
        return Auto(color, peso, ruedas, es_electrico, capacidad_pasajeros)
    elif tipo == 'moto':
        return Moto(color, peso, ruedas, es_electrico, capacidad_pasajeros)
    elif tipo == 'camion':
        return Camion(color, peso, ruedas, es_electrico, capacidad_pasajeros)
    else:
        return Vehiculo(tipo, color, peso, ruedas, es_electrico, capacidad_pasajeros)

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