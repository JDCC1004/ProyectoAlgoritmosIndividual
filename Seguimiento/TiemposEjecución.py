import csv
import os
import timeit
import re
import sys
import bibtexparser
import matplotlib
matplotlib.use("TkAgg")  # Solución para PyCharm

import matplotlib.pyplot as plt

from MetodosOrdenamiento import MetodosOrdenamiento

# Aumentar el límite de recursión para algoritmos recursivos
sys.setrecursionlimit(10000)

# Definir la ruta del archivo .bib con los datos a analizar
ruta = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Datos", "BasesFiltradas.bib")

# Instancia de la clase que contiene los métodos de ordenamiento
metodos = MetodosOrdenamiento()

# Listado de métodos de ordenamiento para datos de texto
metodosTexto = [
    metodos.timSort,
    metodos.combSort,
    metodos.selectionSort,
    metodos.quickSort,
    metodos.heapSort,
    metodos.bitonicSort,
    metodos.gnomeSort,
    metodos.binaryInsertionSort,
    metodos.bubbleSort
]

# Listado de métodos de ordenamiento para datos numéricos
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

# Columnas que contienen valores numéricos en la base de datos
columnasNumericas = ["year", "volume", "number", "pages"]

def convertirAscii(cadena):
    """
    Convierte una cadena en una lista de valores ASCII de cada carácter.
    """
    return [ord(char) for char in cadena]

def extraerNumero(valor):
    """
    Extrae el primer número encontrado en una cadena.
    Retorna el número como entero si lo encuentra, de lo contrario, retorna None.
    """
    match = re.search(r'\d+', valor)
    return int(match.group()) if match else None

def analizarColumna(columnaNombre, entradasBIB):
    """
    Analiza y ordena los valores de una columna específica utilizando distintos algoritmos de ordenamiento.
    Mide y almacena los tiempos de ejecución de cada algoritmo.
    """
    resultados = [] # Lista para almacenar los resultados del análisis
    arregloColumna = [] # Lista con los valores de la columna seleccionada

    # Extraer valores de la columna seleccionada
    for entrada in entradasBIB:
        valorCelda = entrada.get(columnaNombre, '').strip()

        if valorCelda and valorCelda not in ['N/A', 'NULL']:
            if columnaNombre == 'author':
                primerAutor = valorCelda.split(' and ')[0].strip()
                if primerAutor:
                    arregloColumna.append(primerAutor)
            else:
                arregloColumna.append(valorCelda)

    # Determinar si se utilizarán métodos para datos numéricos o de texto
    if columnaNombre in columnasNumericas:
        arregloColumna = [x for x in arregloColumna if x.isdigit()]
        arregloColumna = list(map(int, arregloColumna))
        MetodosOrdenamiento = metodosNumericos
    else:
        arregloColumna = sorted(arregloColumna, key=str.lower)
        MetodosOrdenamiento = metodosTexto

    # Evaluar cada método de ordenamiento
    for metodo in MetodosOrdenamiento:
        print(f"Ordenando {len(arregloColumna)} elementos usando {metodo.__name__}")

        # Medición del tiempo de ejecución con timeit
        tiempoTotal = timeit.timeit(lambda: metodo(arregloColumna[:]), number=10) / 10

        print(f"Tiempo de ejecución para {metodo.__name__}: {tiempoTotal:.6f} segundos")

        resultados.append((columnaNombre, metodo.__name__, len(arregloColumna), tiempoTotal))

    return resultados

# Abrir el archivo .bib y procesar los datos
with open(ruta, 'r', encoding='utf-8') as archivo:
    parser = bibtexparser.load(archivo)
    entradasBIB = parser.entries

    # Identificar las columnas disponibles en la base de datos
    columnas = set()
    for entradas in entradasBIB:
        columnas.update(entradas.keys())

    columnas = list(columnas)
    print("Columnas disponibles:")
    for i, columna in enumerate(columnas):
        print(f"{i + 1}. {columna}")

    # Solicitar al usuario que seleccione una columna para analizar
    columnaSeleccionada = int(input("Seleccione el número de la columna a analizar: ")) - 1

# Validar la selección del usuario
if 0 <= columnaSeleccionada < len(columnas):
    # Obtener el nombre de la columna seleccionada por el usuario
    columnaNombre = columnas[columnaSeleccionada]
    print(f"Columna seleccionada: {columnaNombre}\n")

    # Analizar la columna seleccionada utilizando diferentes métodos de ordenamiento
    resultados = analizarColumna(columnaNombre, entradasBIB)

    # Definir los nombres de las carpetas donde se guardarán los resultados y gráficos
    carpeta_resultados = "resultados"
    carpeta_graficas = "graficas"

    # Crear las carpetas si no existen para almacenar los archivos generados
    os.makedirs(carpeta_resultados, exist_ok=True)
    os.makedirs(carpeta_graficas, exist_ok=True)

    # Generar nombres de archivos dinámicos basados en la columna analizada
    nombre_archivo_csv = os.path.join(carpeta_resultados, f"resultados_tiempos_{columnaNombre}.csv")
    nombre_archivo_png = os.path.join(carpeta_graficas, f"grafico_tiempos_{columnaNombre}.png")

    # Guardar los resultados del análisis en un archivo CSV con la estructura adecuada
    with open(nombre_archivo_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Columna", "Método", "Tamaño", "Tiempo (s)"])
        writer.writerows(resultados)

    print(f"\n📂 Resultados guardados en '{nombre_archivo_csv}'.")

    # Extraer los nombres de los métodos de ordenamiento y los tiempos de ejecución
    metodos = [r[1] for r in resultados]
    tiempos = [r[3] for r in resultados]

    # Generar un gráfico de barras para visualizar los tiempos de ejecución
    plt.figure(figsize=(10, 6))
    plt.barh(metodos, tiempos, color='skyblue')
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Método")
    plt.title(f"Tiempos de ejecución de algoritmos ({columnaNombre})")
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.savefig(nombre_archivo_png)  # Guarda el gráfico en un archivo con el nombre dinámico

    print(f"📊 Gráfico guardado como '{nombre_archivo_png}'. Ábrelo manualmente.")


else:
    # Mensaje de error en caso de que la selección del usuario sea inválida
    print("Selección inválida.")