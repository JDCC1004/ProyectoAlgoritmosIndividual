import os
import glob
import re

rutaArchivos = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Data")

if not os.path.exists(rutaArchivos):
    print(f"Error: La carpeta {rutaArchivos} no existe.")
    exit()

basesUnificadas = os.path.join(rutaArchivos, "BasesUnificadas.bib")
basesFiltradas = os.path.join(rutaArchivos, "BasesFiltradas.bib")
basesRepetidas = os.path.join(rutaArchivos, "BasesRepetidas.bib")


# Unificar archivos .bib

archivos = glob.glob(os.path.join(rutaArchivos, "*.bib"))

if not archivos:
    print("No se encontraron archivos .bib en la carpeta especificada.")
    exit()

with open(basesUnificadas, "w", encoding="utf-8") as salida:
    for archivo in archivos:
        with open(archivo, "r", encoding="utf-8") as entrada:
            salida.write(entrada.read() + "\n")

print(f"Bases de datos unificadas en:  {basesUnificadas}")

# Filtro de entradas repetidas

entradasUnicas = {}
entradasRepetidas = {}

patronTitulo = re.compile(r"title\s*=\s*\{([^}]+)\}", re.IGNORECASE)


with open(basesUnificadas, "r", encoding="utf-8") as entrada:
    contenido = entrada.read()
    partes = contenido.split("\n@")
    if partes[0].strip():
        partes[0] = "@" + partes[0]

    for entrada in partes:
        entrada = entrada.strip()
        if not entrada:
            continue

        coincidenciaTitulo = patronTitulo.search(entrada)
        titulo = coincidenciaTitulo.group(1).strip() if coincidenciaTitulo else None

        if titulo:
            tituloNormalizado = titulo.lower()
            if tituloNormalizado in entradasUnicas:
                entradasRepetidas[tituloNormalizado] = entrada
            else:
                entradasUnicas[tituloNormalizado] = entrada
        else:
            claveGenerica = f"Unica_{len(entradasUnicas) + 1}"
            entradasUnicas[claveGenerica] = entrada


with open(basesFiltradas, "w", encoding="utf-8") as salidaFiltrada:
    for entrada in entradasUnicas.values():
        salidaFiltrada.write(entrada + "\n\n")

with open(basesRepetidas, "w", encoding="utf-8") as salidaRepetidas:
    for entrada in entradasRepetidas.values():
        salidaRepetidas.write(entrada + "\n\n")

print(f"Archivo filtrado en: {basesFiltradas} ({len(entradasUnicas)} entradasUnicas).")
print(f"Archivo de entradas repetidas en: {basesRepetidas} ({len(entradasRepetidas)} entradasRepetidas).")