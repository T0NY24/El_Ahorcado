import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = {}

class ArbolAhorcado:
    def __init__(self):
        self.raiz = Nodo(None)

    def agregar_palabra(self, palabra):
        nodo_actual = self.raiz
        for letra in palabra:
            if letra not in nodo_actual.hijos:
                nodo_actual.hijos[letra] = Nodo(letra)
            nodo_actual = nodo_actual.hijos[letra]

    def elegir_palabra(self):
        nodo_actual = self.raiz
        while nodo_actual.hijos:
            nodo_actual = random.choice(list(nodo_actual.hijos.values()))
        palabra = ""
        while nodo_actual.valor:
            palabra += nodo_actual.valor
            nodo_actual = self.raiz
            while nodo_actual.hijos:
                if nodo_actual.valor:
                    nodo_actual = random.choice(list(nodo_actual.hijos.values()))
                else:
                    break
        return palabra

def mostrar_muñeco(intentos):
    if intentos >= 6:
        print("Perdiste, vuelve a intentarlo.")
        return
    muñeco = [
        "  +---+",
        "  |   |",
        "  |     ",
        "  |     ",
        "  |     ",
        "  |     ",
        "========="
    ]
    partes_muñeco = [
        "  O   ",
        " /|\\ ",
        " / \\ "
    ]
    for i in range(intentos):
        if i < len(partes_muñeco):
            muñeco[2+i] = muñeco[2+i][:4] + partes_muñeco[i] + muñeco[2+i][len(partes_muñeco[i])+4:]
    for linea in muñeco:
        print(linea)


def jugar_ahorcado():
    arbol = ArbolAhorcado()
    for palabra in ["gato", "perro", "casa", "sol", "luna"]:
        arbol.agregar_palabra(palabra)

    while True:
        palabra_secreta = arbol.elegir_palabra()
        letras_adivinadas = set()
        intentos = 0

        print("Bienvenido al juego del ahorcado")
        print("Escoja una opción:")
        print("1. Jugar")
        print("2. Salir")

        opcion = input(">> ")

        if opcion == "2":
            return

        while True:
            palabra_actual = "".join(
                letra if letra in letras_adivinadas else "_" for letra in palabra_secreta
            )
            print(f"Palabra: {palabra_actual}")

            if intentos > 0:
                print("Muñeco:")
                mostrar_muñeco(intentos)

            letra = input("Adivina una letra (o presiona '0' para salir): ").lower()

            if letra == '0':
                return

            if letra in letras_adivinadas:
                print("¡Ya adivinaste esa letra!")
                continue

            if letra in palabra_secreta:
                letras_adivinadas.add(letra)
                print("¡Bien hecho!")

                if set(palabra_secreta) == letras_adivinadas:
                    print(f"¡Felicidades! Adivinaste la palabra '{palabra_secreta}'")
                    break

            else:
                print("¡Esa letra no está!")
                intentos += 1

                if intentos == 6:
                    mostrar_muñeco(intentos)
                    print("Perdiste, vuelve a intentarlo.")
                    break

        while True:
            opcion = input("¿Qué deseas hacer? 1. Jugar nuevamente 2. Salir: ")
            if opcion == "1" or opcion == "2":
                break

        if opcion == "2":
            return

# Iniciar el juego
jugar_ahorcado()
