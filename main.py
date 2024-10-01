def obtener_numero_natural():
    while True:
        try:
            numero = int(input("Introduce un número natural: "))
            if numero < 1:
                raise ValueError("El número debe ser un natural (mayor o igual a 1).")
            return numero
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, intenta de nuevo.")

def calcular_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def main():
    numero = obtener_numero_natural()
    divisores = calcular_divisores(numero)
    print(f"Los divisores de {numero} son: {divisores}")

if __name__ == "__main__":
    main()