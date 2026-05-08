def knapsack_fraccionado(articulos, W):
    for a in articulos:
        a["ratio"] = a["p"] / a["w"]

    articulos.sort(key=lambda a: a["ratio"], reverse=True)

    capacidad_restante = W
    valor_total = 0.0
    tomado = []

    print(f"  Capacidad W = {W}u")
    print(f"  {'Articulo':>10} | {'ratio p/w':>10} | {'disponible':>10} | {'tomado':>8} | {'valor añadido':>14} | {'restante':>10}")
    print(f"  {'-'*74}")

    for a in articulos:
        if capacidad_restante == 0:
            break
        cantidad = min(a["w"], capacidad_restante)
        valor_ganado = cantidad * a["ratio"]
        valor_total += valor_ganado
        capacidad_restante -= cantidad
        tomado.append({"nombre": a["nombre"], "cantidad": cantidad, "valor": valor_ganado, "w_total": a["w"]})
        print(f"  {a['nombre']:>10} | {a['ratio']:>10.2f} | {a['w']:>9}u | {cantidad:>7}u | {valor_ganado:>13.2f} | {capacidad_restante:>9}u")

    return valor_total, tomado


def mostrar_caso(numero, articulos, W, descripcion):
    print()
    print("=" * 76)
    print(f"  CASO #{numero}: {descripcion}")
    print("=" * 76)

    valor, tomado = knapsack_fraccionado(articulos, W)

    print()
    print("  RESULTADO:")
    for t in tomado:
        fraccion = f"({t['cantidad']}/{t['w_total']}u)"
        print(f"    {t['nombre']:>10}: {t['cantidad']:>5}u tomadas {fraccion:>10}  ->  valor ${t['valor']:.2f}")
    print(f"  {'─'*50}")
    print(f"    VALOR TOTAL: ${valor:.2f}")
    print()


def run():
    print()
    print("╔══════════════════════════════════════════════════════════════════════════╗")
    print("║          ALGORITMO GREEDY — KNAPSACK FRACCIONADO                        ║")
    print("║   Paradigma: Greedy · Ordenar por ratio p/w desc · O(n log n)           ║")
    print("╚══════════════════════════════════════════════════════════════════════════╝")

    mostrar_caso(1,
        [
            {"nombre": "item1", "p": 60,  "w": 10},
            {"nombre": "item2", "p": 100, "w": 20},
            {"nombre": "item3", "p": 120, "w": 30},
        ],
        W=50,
        descripcion="Instancia del apendice (W=50u, 3 articulos)"
    )

    mostrar_caso(2,
        [
            {"nombre": "oro",    "p": 500, "w": 10},
            {"nombre": "plata",  "p": 300, "w": 20},
            {"nombre": "bronce", "p": 200, "w": 50},
        ],
        W=40,
        descripcion="Fuerza fraccion en ultimo articulo (W=40u)"
    )

    mostrar_caso(3,
        [
            {"nombre": "diamante",  "p": 1000, "w":  5},
            {"nombre": "rubi",      "p":  400, "w": 15},
            {"nombre": "esmeralda", "p":  300, "w": 25},
            {"nombre": "topacio",   "p":  150, "w": 30},
        ],
        W=45,
        descripcion="Articulo de mayor ratio con poco peso (W=45u, 4 articulos)"
    )

    print("=" * 76)
    print("  Complejidad temporal: O(n log n)  — dominado por el ordenamiento")
    print("  Complejidad espacial: O(n)         — arreglo de cantidades tomadas")
    print("=" * 76)
    print()


if __name__ == "__main__":
    run()
