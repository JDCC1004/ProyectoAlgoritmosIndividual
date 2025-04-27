import os
import csv
import matplotlib.pyplot as plt

def graficarResultados(resultados):

    rutaGrafica = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Resultados", "Graficas")
    rutaReporte = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Resultados", "Reportes")

    # Crear directorios si no existen
    os.makedirs(rutaGrafica, exist_ok=True)
    os.makedirs(rutaReporte, exist_ok=True)

    nombreArchivoCSV = os.path.join(rutaReporte, f"Tiempo Ejecución.csv")
    nombreArchivoPNG = os.path.join(rutaGrafica, f"Gráfica Tiempo Ejecución.png")

    resultados = sorted(resultados, key=lambda x: x[1], reverse=True)  # Ordenar por tiempo de ejecución
    
    metodos = [resultado[0] for resultado in resultados]
    tiempos = [resultado[1] for resultado in resultados]

    ' Archivos CSV '
    with open(nombreArchivoCSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Método", "Tiempo (s)"])
        for metodo, tiempo in resultados:
            writer.writerow([metodo, tiempo])

    print(f"\n📂 Resultados guardados en '{nombreArchivoCSV}'.")

    ' Gráfica de Resultados '
    plt.figure(figsize=(10, 6))
    plt.barh(metodos, tiempos, color='skyblue')
    plt.xlabel('Tiempo Promedio (s)')
    plt.title('Tiempos de Ejecución de Métodos de Ordenamiento')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig(nombreArchivoPNG)
    print(f"📊 Gráfico guardado como '{nombreArchivoPNG}'")