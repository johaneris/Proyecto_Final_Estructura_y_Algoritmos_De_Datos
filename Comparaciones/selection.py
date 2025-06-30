import sys
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i # Elemento con menos valor
        for j in range(i + 2, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambio 
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
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
    selection_sort(datos)
    fin = time.time()
    
    print(f"Tiempo de ejecución: {fin-inicio:.4f} segundos")
    
if __name__ == "__main__":
    main()