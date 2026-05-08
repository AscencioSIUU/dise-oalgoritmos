import hacer_sencillo
import knapsack
import nokia


def menu():
    print()
    print("╔══════════════════════════════════════════════╗")
    print("║            PARCIAL 2 — ALGORITMOS            ║")
    print("╠══════════════════════════════════════════════╣")
    print("║  1. Hacer Sencillo (cambio de monedas)       ║")
    print("║  2. Knapsack Fraccionado                     ║")
    print("║  3. Nokia 3230 Combinaciones                 ║")
    print("║  4. Todos                                    ║")
    print("║  0. Salir                                    ║")
    print("╚══════════════════════════════════════════════╝")
    print()


def main():
    while True:
        menu()
        opcion = input("  Seleccione una opcion: ").strip()

        if opcion == "1":
            hacer_sencillo.run()
        elif opcion == "2":
            knapsack.run()
        elif opcion == "3":
            nokia.run()
        elif opcion == "4":
            hacer_sencillo.run()
            knapsack.run()
            nokia.run()
        elif opcion == "0":
            print("\n  Saliendo...\n")
            break
        else:
            print("\n  Opcion invalida. Intente de nuevo.")


if __name__ == "__main__":
    main()
