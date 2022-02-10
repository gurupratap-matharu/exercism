lista = ["miel", "extraterrestre", "al", "automovil", "auto", "revestir"]
alfabeto = "zyxwvutsrqponmlkjihgfedcba"


def ordenar_extraterrestre(desordenadas, orden_alfabeto):
    """Orders a list of words based on custom alphabet order"""

    ordenada = sorted(
        desordenadas, key=lambda word: [orden_alfabeto.index(char) for char in word]
    )
    return ordenada


if __name__ == "__main__":
    print(ordenar_extraterrestre(lista, alfabeto))
