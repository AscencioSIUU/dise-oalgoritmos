def hacer_sencillo(m):
    denominaciones = [25, 10, 5, 1]
    total = 0
    resultado = []
    restante = m

    print(f"  Monto inicial: {m} centavos")
    print(f"  {'Denominacion':>12} | {'cantidad = floor(m/d)':>22} | {'Restante':>10}")
    print(f"  {'-'*54}")

    for d in denominaciones:
        cantidad = restante // d
        if cantidad > 0:
            resultado.append((d, cantidad))
            total += cantidad
            restante = restante % d
            print(f"  {d:>10}¢  | {f'floor({restante + cantidad*d}/{d}) = {cantidad}':>22} | {restante:>8}¢")
        else:
            print(f"  {d:>10}¢  | {'no aplica (0 monedas)':>22} | {restante:>8}¢")

    return total, resultado


def mostrar_caso(numero, m, descripcion):
    print()
    print("=" * 60)
    print(f"  CASO DE PRUEBA #{numero}: {descripcion}")
    print(f"  Monto a devolver: {m} centavos (Q{m/100:.2f})")
    print("=" * 60)

    total, resultado = hacer_sencillo(m)

    print()
    print("  RESULTADO:")
    for d, cantidad in resultado:
        nombre = {25: "veinticinco", 10: "diez", 5: "cinco", 1: "un"}[d]
        print(f"    {cantidad:>3} moneda(s) de {d:>2}¢  ({nombre} centavos)")
    print(f"  {'─'*35}")
    print(f"    TOTAL DE MONEDAS: {total}")
    print()


def main():
    print()
    print("╔══════════════════════════════════════════════════════════╗")
    print("║         ALGORITMO GREEDY — HACER SENCILLO                ║")
    print("║   Denominaciones: {1, 5, 10, 25} centavos                ║")
    print("║   Paradigma: Greedy (selección voraz en orden desc.)      ║")
    print("╚══════════════════════════════════════════════════════════╝")

    # Caso 1: instancia del examen
    mostrar_caso(
        1, 293,
        "Instancia del examen (Q2.93)"
    )

    # Caso 2: monto que NO se puede cubrir eficientemente con denominaciones menores
    mostrar_caso(
        2, 99,
        "Maximo sin llegar a Q1.00 (99¢)"
    )

    # Caso 3: monto que obliga a usar solo monedas de 1 (sin multiplos de 5/10/25)
    mostrar_caso(
        3, 41,
        "Monto sin multiplos de 5 (41¢)"
    )

    print("=" * 60)
    print("  Complejidad temporal: O(|D|) = O(4) = O(1)")
    print("  Complejidad espacial: O(|D|) = O(1)")
    print("  Propiedad greedy: la eleccion local optima (moneda")
    print("  mas grande que cabe) produce el optimo global porque")
    print("  las denominaciones {1,5,10,25} satisfacen la")
    print("  greedy-choice property sobre los enteros positivos.")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
