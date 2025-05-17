from flota import Flota
from vehiculo import imprimir_datos_vehiculo

def leer_datos_vehiculo():
    tipos_validos = ['auto', 'moto', 'camión']
    while True:
        tipo = input("Tipo (auto/moto/camión): ").lower()
        if tipo in tipos_validos:
            break
        print("Tipo inválido. Debe ser 'auto', 'moto' o 'camión'.")
    while True:
        color = input("Color: ").strip()
        if color:
            break
        print("El color no puede estar vacío.")
    while True:
        try:
            peso = float(input("Peso (kg): "))
            if peso > 0:
                break
            else:
                print("El peso debe ser un número positivo.")
        except ValueError:
            print("Por favor, ingrese un número válido para el peso.")
    if tipo == 'moto':
        ruedas = 2
        capacidad = 2
    else:
        ruedas = 4
        capacidad = 5 if tipo == 'auto' else 2
    while True:
        electrico_input = input("Es eléctrico? (s/n): ").lower()
        if electrico_input in ['s', 'n']:
            electrico = electrico_input == 's'
            break
        print("Respuesta inválida. Escriba 's' para sí o 'n' para no.")
    return tipo, color, peso, ruedas, electrico, capacidad

if __name__ == "__main__":
    flota = Flota()
    while True:
        print("\n1. Agregar vehículo")
        print("2. Mostrar reporte")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            datos = leer_datos_vehiculo()
            flota.agregar_vehiculo(*datos)
        elif opcion == '2':
            flota.generar_reporte()
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
