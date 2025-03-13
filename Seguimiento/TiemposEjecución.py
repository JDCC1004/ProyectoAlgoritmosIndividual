import os
import time
import re
import sys
import bibtexparser

from MetodosOrdenamiento import MetodosOrdenamiento

sys.setrecursionlimit(10000)

ruta = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Data", "BasesUnificadas.bib")

metodos = MetodosOrdenamiento()

metodosTexto = [
    metodos.timSort,
    metodos.combSort,
    metodos.selectionSort,
    metodos.quickSort,
    metodos.heapSort,
    metodos.bitonicSort,
    metodos.gnomeSort,
    metodos.binaryInsertionSort
]

metodosNumericos = [
    metodos.timSort,
    metodos.combSort,
    metodos.selectionSort,
    metodos.quickSort,
    metodos.heapSort,
    metodos.bitonicSort,
    metodos.gnomeSort,
    metodos.binaryInsertionSort,
    metodos.pigeonholeSort,
    metodos.bucketSort,
    metodos.radixSort,
    metodos.treeSort
]

columnasNumericas = ["year", "volume", "number", "pages"]

def convertirAscii(cadena):
    return [ord(char) for char in cadena]

def extraerNumero(valor):
    match = re.search(r'\d+', valor)
    return int(match.group()) if match else None

def analizarColumna(columnaNombre, entradasBIB):
    resultados = []
    arregloColumna = []

    for entrada in entradasBIB:
        valorCelda = entrada.get(columnaNombre, '').strip()

        if columnaNombre == 'author':
            if valorCelda and valorCelda not in ['N/A', 'NULL']:
                primerAutor = valorCelda.split(' and ')[0].strip()
                if primerAutor:
                    arregloColumna.append(primerAutor)

        elif columnaNombre in columnasNumericas and valorCelda.isdigit():
                arregloColumna.append(int(valorCelda))

        else:
            if valorCelda and valorCelda not in ['N/A', 'NULL']:
                arregloColumna.append(valorCelda)

    if columnaNombre in columnasNumericas:
        arregloColumna = [x for x in arregloColumna if isinstance(x, int)]
        MetodosOrdenamiento = metodosNumericos
    else:
        if columnaNombre == 'author':
            arregloColumna = [sum(convertirAscii(x) for x in arregloColumna)]
            MetodosOrdenamiento = metodosNumericos
        else:
            MetodosOrdenamiento = metodosTexto

    for metodos in MetodosOrdenamiento:
        inicioTiempo = time.time()

        arregloOrdenado = metodos(arregloColumna[:])

        finalTiempo = time.time()
        timepoTotal = finalTiempo - inicioTiempo

        print(timepoTotal)

        resultados.append((columnaNombre, metodos.__name__, len(arregloColumna),timepoTotal))

    return resultados

with open(ruta, 'r', encoding='utf-8') as archivo:
    parser = bibtexparser.load(archivo)
    entradasBIB = parser.entries

    columnas = set()
    for entradas in entradasBIB:
        columnas.update(entradas.keys())

    columnas = list(columnas)
    print("Columnas disponibles:")
    for i, columna in enumerate(columnas):
        print(f"{i + 1}. {columna}")

    columnaSeleccionada = int(input("Seleccione el número de la columna a analizar: ")) - 1

    if 0 <= columnaSeleccionada < len(columnas):
        columnaNombre = columnas[columnaSeleccionada]
        print(f"Columna seleccionada: {columnaNombre}\n")

        resultados = analizarColumna(columnaNombre, entradasBIB)
    else:
        print("Selección inválida.")