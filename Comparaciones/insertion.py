import sys
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

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
    insertion_sort(datos)
    fin = time.time()
    
    print(f"Tiempo de ejecución: {fin-inicio:.4f} segundos")
    
if __name__ == "__main__":
    main()