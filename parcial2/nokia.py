VECINOS = {
    0: [0, 8],
    1: [1, 2, 4],
    2: [1, 2, 3, 5],
    3: [2, 3, 6],
    4: [1, 4, 5, 7],
    5: [2, 4, 5, 6, 8],
    6: [3, 5, 6, 9],
    7: [4, 7, 8],
    8: [0, 5, 7, 8, 9],
    9: [6, 8, 9],
}


def nokia_combinaciones(n):
    anterior = {d: 1 for d in range(10)}

    print(f"  {'k':>4} | {'dp[0]':>6} {'dp[1]':>6} {'dp[2]':>6} {'dp[3]':>6} {'dp[4]':>6} {'dp[5]':>6} {'dp[6]':>6} {'dp[7]':>6} {'dp[8]':>6} {'dp[9]':>6} | {'total':>8}")
    print(f"  {'-'*101}")

    total_k1 = sum(anterior.values())
    vals = "  ".join(f"{anterior[d]:>6}" for d in range(10))
    print(f"  {1:>4} | {vals} | {total_k1:>8}")

    for k in range(2, n + 1):
        actual = {}
        for d in range(10):
            actual[d] = sum(anterior[v] for v in VECINOS[d])
        anterior = actual
        total_k = sum(anterior.values())
        vals = "  ".join(f"{anterior[d]:>6}" for d in range(10))
        print(f"  {k:>4} | {vals} | {total_k:>8}")

    return sum(anterior.values()), anterior


def mostrar_caso(numero, n, descripcion, esperado=None):
    print()
    print("=" * 103)
    print(f"  CASO #{numero}: {descripcion}  (n={n})")
    print("=" * 103)

    total, dp_final = nokia_combinaciones(n)

    print()
    print("  RESULTADO:")
    print(f"    Longitud de secuencia : {n}")
    print(f"    Total de combinaciones: {total}", end="")
    if esperado is not None:
        estado = "✓" if total == esperado else f"✗ (esperado {esperado})"
        print(f"  {estado}", end="")
    print()
    print()


def run():
    print()
    print("╔══════════════════════════════════════════════════════════════════════════╗")
    print("║       PROGRAMACION DINAMICA — NOKIA 3230 COMBINACIONES                  ║")
    print("║   Paradigma: DP bottom-up · Recurrencia: f(d,k) = Σ f(d',k-1)          ║")
    print("╚══════════════════════════════════════════════════════════════════════════╝")

    mostrar_caso(1, 1, "Caso base — un digito cualquiera",          esperado=10)
    mostrar_caso(2, 2, "Instancia del apendice",                    esperado=36)
    mostrar_caso(3, 3, "Secuencias de longitud 3",                  esperado=138)

    print("=" * 103)
    print("  Complejidad temporal: O(n)   — 10 digitos x max 5 vecinos = constante por paso")
    print("  Complejidad espacial: O(1)   — rolling array, solo dos filas de 10 valores")
    print("=" * 103)
    print()


if __name__ == "__main__":
    run()
