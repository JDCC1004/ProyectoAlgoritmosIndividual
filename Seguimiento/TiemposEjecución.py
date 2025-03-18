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

        if valorCelda and valorCelda not in ['N/A', 'NULL']:
            if columnaNombre == 'author':
                primerAutor = valorCelda.split(' and ')[0].strip()
                if primerAutor:
                    arregloColumna.append(primerAutor)
            else:
                arregloColumna.append(valorCelda)

    if columnaNombre in columnasNumericas:
        arregloColumna = [x for x in arregloColumna if x.isdigit()]
        arregloColumna = list(map(int, arregloColumna))
        MetodosOrdenamiento = metodosNumericos
    else:
        arregloColumna = sorted(arregloColumna, key=str.lower)
        MetodosOrdenamiento = metodosTexto

    for metodos in MetodosOrdenamiento:

        print(f"Ordenando {len(arregloColumna)} elementos usando {metodos.__name__}")

        inicioTiempo = time.time()

        arregloOrdenado = metodos(arregloColumna[:])

        finalTiempo = time.time()
        tiempoTotal = finalTiempo - inicioTiempo

        print(f"Tiempo de ejecución para {metodos.__name__}: {tiempoTotal:.6f} segundos")

        resultados.append((columnaNombre, metodos.__name__, len(arregloColumna),tiempoTotal))

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