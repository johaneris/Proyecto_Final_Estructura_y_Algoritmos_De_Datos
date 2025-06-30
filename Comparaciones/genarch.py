import random

def generar_random():
    with open("random.txt", "w") as archivo:
        for _ in range(10000):
            numero = random.randint(1, 10000)
            archivo.write(f"{numero}\n")

def generar_sorted():
    with open("sorted.txt", "w") as archivo:
        for numero in range(1, 10001):
            archivo.write(f"{numero}\n")

def generar_reversed():
    with open("reversed.txt", "w") as archivo:
        for numero in range(10000, 0, -1):
            archivo.write(f"{numero}\n")

def main():
    print("Generando archivos...")
    generar_random()
    generar_sorted()
    generar_reversed()
    print("¡Archivos generados con éxito!")

if __name__ == "__main__":
    main()
