import time
import re

from MetodosOrdenamiento import MetodosOrdenamiento

ruta = './Data/BasesFiltrafas.bib'

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