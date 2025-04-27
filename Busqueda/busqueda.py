import os
import re
from collections import Counter

lista = ["Abstraction", "Algorithm", "Coding", "Creativity", "Logic",
         "Conditionals", "Loops", "Motivation", "Persistence", "Block",
         "Mobile Application", "Programming", "Robotic", "Scratch"
         ]

lista = [p.lower() for p in lista]

def extraerAbstract(archivo):
    with open (archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()

    entradas = contenido.split('@')[1:]

    abstracts = []
    for entrada in entradas:
        match = re.search(r'abstract\s*=\s*\{([^}]+)\}', entrada, re.IGNORECASE | re.DOTALL)
        if match:
            abstract = match.group(1).replace('\n', ' ')
            abstracts.append(abstract.lower())
    return abstracts

def buscarPalabrasClave(abstracts, lista):
    resumen = [0] * len(lista)
    for abstract in abstracts:
        for i, palabra in enumerate(lista):
            resumen[i] += len(re.findall(r'\b' + re.escape(palabra) + r'\b', abstract))
    return resumen

rutaArchivos = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Datos")
archivo = os.path.join(rutaArchivos, "BasesFiltradas.bib")

abstracts = extraerAbstract(archivo)
frecuencias = buscarPalabrasClave(abstracts, lista)

print (f"Frecuencias de aparición por palabra:")
print (frecuencias)