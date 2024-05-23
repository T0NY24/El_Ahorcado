# TDA
# Juego del Ahorcado

Este es un simple juego del ahorcado implementado en Python.

## Descripción

El juego del ahorcado es un juego de adivinanzas donde el jugador intenta adivinar una palabra oculta letra por letra. El jugador tiene un número limitado de intentos antes de perder el juego. El objetivo es adivinar la palabra antes de que se agoten los intentos y se complete la figura del ahorcado.

## Estructura del Código

### Clase `Nodo`

- **Descripción**: Representa un nodo en la estructura de datos del árbol del ahorcado.
- **Atributos**:
  - `valor`: El valor almacenado en el nodo (en este caso, una letra).
  - `hijos`: Un diccionario que almacena los nodos hijos del nodo actual.

### Clase `ArbolAhorcado`

- **Descripción**: Representa el árbol del ahorcado, que contiene todas las palabras disponibles para el juego.
- **Métodos**:
  - `agregar_palabra(palabra)`: Agrega una palabra al árbol del ahorcado.
  - `elegir_palabra()`: Elige una palabra aleatoria del árbol del ahorcado para que el jugador la adivine.

### Función `mostrar_muñeco`

- **Descripción**: Muestra la representación visual del ahorcado según el número de intentos.
- **Parámetros**:
  - `intentos`: El número de intentos que ha realizado el jugador.

### Función `jugar_ahorcado`

- **Descripción**: Inicia el juego del ahorcado.
- **Flujo del Juego**:
  1. Agrega palabras al árbol del ahorcado.
  2. Muestra un menú para que el jugador elija jugar o salir.
  3. Si elige jugar, elige una palabra aleatoria y comienza el juego.
  4. El jugador intenta adivinar la palabra, letra por letra.
  5. Muestra el estado actual de la palabra y el muñeco del ahorcado.
  6. Si el jugador adivina la palabra o se quedan sin intentos, se muestra un mensaje apropiado.
  7. Pregunta al jugador si desea jugar nuevamente o salir.

## Instrucciones de Ejecución

1. Asegúrate de tener Python instalado en tu sistema.
2. Ejecuta el script `Hanged.py`.
3. Sigue las instrucciones en pantalla para jugar al ahorcado.

¡Disfruta del juego!

--- 