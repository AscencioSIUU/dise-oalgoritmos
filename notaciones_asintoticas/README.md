# Análisis de Algoritmos de Ordenamiento

Este proyecto implementa y analiza el tiempo de ejecución de los algoritmos **Insertion Sort** y **Merge Sort**.

## Estructura del Proyecto

- `insertion_sort.py` - Implementación del algoritmo Insertion Sort
- `merge_sort.py` - Implementación del algoritmo Merge Sort
- `analisis_tiempos.py` - Script para medir y comparar tiempos de ejecución
- `requirements.txt` - Dependencias del proyecto

## Instalación

1. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Ejecutar análisis completo:
```bash
python analisis_tiempos.py
```

Este script:
- Prueba ambos algoritmos con diferentes tamaños de arreglos
- Compara tiempos en tres escenarios: aleatorio, ordenado e inverso
- Genera gráficas comparativas
- Muestra conclusiones sobre el rendimiento

### Ejecutar algoritmos individuales:
```bash
python insertion_sort.py
python merge_sort.py
```

## Complejidad Temporal

### Insertion Sort
- **Mejor caso**: O(n) - arreglo ya ordenado
- **Caso promedio**: O(n²)
- **Peor caso**: O(n²) - arreglo en orden inverso

### Merge Sort
- **Mejor caso**: O(n log n)
- **Caso promedio**: O(n log n)
- **Peor caso**: O(n log n)

## Resultados Esperados

- Para arreglos pequeños (n < 50), Insertion Sort puede ser competitivo
- Para arreglos grandes, Merge Sort es significativamente más rápido
- Merge Sort tiene rendimiento consistente independiente del orden inicial
