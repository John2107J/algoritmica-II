def multiplicar_matrices(A, B):
    """Funcion que multiplica 2 matrices y retorna C como resultado de AxB"""

    x = len(A)        # filas de A
    y = len(A[0])     # columnas de A = filas de B
    z = len(B[0])     # columnas de B

    # Inicializar C con ceros
    C = [[0] * z for _ in range(x)]

    ops = 0  # contador de operaciones (multiplicaciones + sumas)

    # Triple bucle anidado, la razon por la que es n³
    for i in range(x):          # filas de A
        for j in range(z):      # columnas de B
            for k in range(y):  # dimensión compartida
                C[i][j] += A[i][k] * B[k][j]
                ops += 2        # 1 multiplicación + 1 suma

    return C, ops


def crear_matriz_identidad(n):
    """Crea una matriz identidad nxn (para pruebas rápidas)."""
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def crear_matriz_unos(filas, columnas):
    """Crea una matriz de unos filasxcolumnas."""
    return [[1] * columnas for _ in range(filas)]

# Demostración con matrices 
# MULTIPLICACION DE 2 MATRICES 2X3 Y 3X2

A = [[1, 2, 3],
     [4, 5, 6]]   # 2×3

B = [[7,  8],
     [9,  10],
     [11, 12]]    # 3×2

C, ops = multiplicar_matrices(A, B)

"""MUESTRO POR PANTALLA LAS MATRICES A CALCULAR"""
print(f"\nA (2x3):")
for fila in A:
    print(f"  {fila}")

print(f"\nB (3x2):")
for fila in B:
    print(f"  {fila}")

print(f"\nC = A x B (2x2):")
for fila in C:
    print(f"  {fila}")

print(f"\nOperaciones realizadas: {ops}")
print(f"Fórmula teorica 2·x·y·z = 2·2·3·2 = {2*2*3*2}")
print()
print(f"\n{'n':>6} | {'Ops reales':>12} | {'2·n³ (en teoria)':>16} | {'Coincide':>9}")

"""Operacion para matrices cuadradas"""
for n in [10, 20, 50]:
    A_n = crear_matriz_unos(n, n)
    B_n = crear_matriz_unos(n, n)
    _, ops_n = multiplicar_matrices(A_n, B_n)
    teorico = 2 * n**3
    coincide = "Si" if ops_n == teorico else "No"

    """Hago un print para realizar una tabla que muestre el analisis ralizado"""
    print(f"{n:>6} | {ops_n:>12,} | {teorico:>16,} | {coincide:>9}")


"""cada iteracion del bucle interno ejecuta
    1 multiplicacion + 1 suma = 2 operaciones
    Total teorico: 2n³"""