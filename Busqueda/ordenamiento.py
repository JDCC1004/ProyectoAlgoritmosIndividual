import timeit

from tabulate import tabulate
from busqueda import frecuencias, lista
from MetodosOrdenamientoTuplas import MetodosOrdenamientoTuplas
from Graficas import graficarResultados

frecuencias

frecuenciaTuplas = list(zip(lista, frecuencias))
frecuenciaTuplasCP = frecuenciaTuplas.copy()

ordenador = MetodosOrdenamientoTuplas()

metodos = {
    'TimSort': ordenador.timSort,
    'CombSort': ordenador.combSort,
    'SelectionSort': ordenador.selectionSort,
    'QuickSort': ordenador.quickSort,
    'HeapSort': ordenador.heapSort,
    'BitonicSort': ordenador.bitonicSort,
    'GnomeSort': ordenador.gnomeSort,
    'BinaryInsertionSort': ordenador.binaryInsertionSort,
    'BubbleSort': ordenador.bubbleSort,
    'PigeonholeSort': ordenador.pigeonholeSort,
    'BucketSort': ordenador.bucketSort,
    'RadixSort': ordenador.radixSort,
    'TreeSort': ordenador.treeSort
}

resultados = []

for nombre, metodo in metodos.items():
    print(f"Ejecutando {metodo.__name__}...")
    tiempoTotal = timeit.timeit(lambda: metodo(frecuenciaTuplas.copy()), number=1)        
    print(f"Tiempo promedio: {tiempoTotal:.6f} segundos")
    resultados.append((metodo.__name__, tiempoTotal))

print(f"\nFrecuencias de aparición:\n")
frecuenciaTuplasCP = sorted(frecuenciaTuplas, key=lambda x: x[1], reverse=True)
print(tabulate(frecuenciaTuplasCP, headers=['Término', 'Frecuencia'], tablefmt='grid'))
print(f"\nResultados de los métodos de ordenamiento:\n")
print(tabulate(resultados, headers=['Método', 'Tiempo (s)'], tablefmt='grid'))
    
graficarResultados(resultados)