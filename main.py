class CalculadoraRaizCuadrada:
    def __init__(self, a: float, iteraciones: int = 10):
        self.a = a
        self.iteraciones = iteraciones
        self.x = 1.0  # Valor inicial

    def calcular_raiz(self) -> float:
        for k in range(1, self.iteraciones + 1):
            self.x = (self.x + self.a / self.x) / 2
            print(f"La raíz después de {k} iteraciones es {self.x}")
        return self.x

def main():
    try:
        a = float(input("Dame el valor de a: \n"))
        iteraciones = int(input("Dame el número de iteraciones: \n"))

        calculadora = CalculadoraRaizCuadrada(a, iteraciones)
        resultado = calculadora.calcular_raiz()
        print(f"La raíz cuadrada aproximada de {a} es {resultado}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos para 'a' y el número de iteraciones.")

if __name__ == "__main__":
    main()
