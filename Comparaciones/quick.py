import sys
import time

def quicksort(arr):
    """
    Ordena una lista de números usando QuickSort (crea una nueva lista).
    Tiempo promedio: O(n log n)
    Tiempo peor caso: O(n^2)
    """
    if len(arr) <= 1:
        return arr[:]  # ya está ordenada
    pivot = arr[len(arr) // 2]  # elegimos el pivote en la mitad
    menores = [x for x in arr if x < pivot]
    iguales = [x for x in arr if x == pivot]
    mayores = [x for x in arr if x > pivot]
    return quicksort(menores) + iguales + quicksort(mayores)

def cargar_datos(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        return [int(linea.strip()) for linea in archivo.readlines()]
    
def main():
    if len(sys.argv) < 2:
        print("Uso: python ordenar.py <nombre_archivo>")
        sys.exit(1)

    archivo = sys.argv[1]
    datos = cargar_datos(archivo)
    
    inicio = time.time()
    quicksort(datos)
    fin = time.time()
    
    print(f"Tiempo de ejecución: {fin-inicio:.4f} segundos")
    
if __name__ == "__main__":
    main()