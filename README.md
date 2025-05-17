# Problemas de diseño encontrados en el código

## 1. Muchas responsabilidades en una sola clase
La clase `Vehiculo` hace de todo: guarda datos, calcula costos, revisa si necesita inspección e  imprime cosas. Si después quiero cambiar cómo se imprime o cómo se calcula el costo, tengo que meter mano en la misma clase, y eso puede traer problemas.

## 2. Las clases están muy acopladas entre sí
La clase `Flota` depende directamente de cómo está hecha la clase `Vehiculo`. Si cambio algo en `Vehiculo`, capaz que se rompe `Flota`. Además, en el código están juntas, pero igual se importa como si estuvieran separadas, lo cual es confuso.

## 3. Mezcla de lógica y entrada/salida
En el método `agregar_vehiculo` de `Flota` se usan `input()` y `print()` directamente. Esto hace que sea difícil probar el código automáticamente o usarlo en otro tipo de interfaz.

## 4. No se valida lo que pone el usuario
Si el usuario mete un tipo de vehículo raro o un peso negativo, el programa igual lo acepta.

## 5. Hay muchos valores "mágicos" en el código
Los tipos de vehículos, los precios base y los multiplicadores están escritos directo en el código. Si quiero agregar un nuevo tipo de vehículo o cambiar un precio, tengo que buscar y cambiar el código a mano.

## 6. No se usa herencia ni polimorfismo
En vez de tener una clase para cada tipo de vehículo, todo se maneja con `if` y `elif`. Si después quiero agregar más tipos, el código se va a volver cada vez más largo y difícil de leer.
 
---


 ## Cambios y mejoras realizadas

- **Separé responsabilidades:** Ahora la clase `Vehiculo` solo se encarga de los datos y la lógica de cada vehículo. La impresión de datos se hace con una función aparte.
- **Cada clase en su archivo:** Puse `Vehiculo`, `Flota` y el flujo principal (`main.py`) en archivos distintos. Así todo está más modular y menos enredado.
- **Nada de input() en la lógica:** Toda la entrada de datos del usuario se hace fuera de las clases. Las clases solo reciben datos, no preguntan nada.
- **Validación de datos:** Ahora, si el usuario mete algo raro (tipo de vehículo, peso negativo, etc.), el programa le vuelve a preguntar hasta que ponga algo válido.
- **Saqué los valores mágicos:** Los precios base, multiplicadores y extras eléctricos están en constantes al inicio del archivo, así que si hay que cambiar algo, es súper fácil.
- **Herencia y polimorfismo:** Ahora hay subclases para `Auto`, `Moto` y `Camion`, y se usa un factory para crear el tipo correcto de vehículo. Así el código es más limpio y fácil de extender si se agregan más tipos.
