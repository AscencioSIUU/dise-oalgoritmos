import random
from time import perf_counter
from insertionsort import * 
from mergesort import *
import matplotlib.pyplot as plt


# Array sizes to test
arraySizes = [5, 10, 25, 50, 100, 1000, 10000, 50000, 100000]



def measureSortTimes():
    results = []
    for size in arraySizes:
        array = random.sample(range(size * 2), size)  # larger range to avoid duplicates
        arrayInsertion = list(array)
        arrayMerge = list(array)

        # Measure Insertion Sort time
        startInsertion = perf_counter()
        insertion_sort(arrayInsertion)
        endInsertion = perf_counter()
        insertionTime = endInsertion - startInsertion

        # Measure Merge Sort time
        startMerge = perf_counter()
        merge_sort(arrayMerge, 0, len(arrayMerge) - 1)
        endMerge = perf_counter()
        mergeTime = endMerge - startMerge

        results.append({
            'size': size,
            'insertionSort': insertionTime,
            'mergeSort': mergeTime
        })
        print(f"Size: {size:>7} | Insertion: {insertionTime:.6f} s | Merge: {mergeTime:.6f} s")
    return results



def main():
    print("Comparison of Insertion Sort and Merge Sort times for various sizes:")
    print("-" * 60)
    results = measureSortTimes()

    # Plot results
    sizes = [r['size'] for r in results]
    insertionTimes = [r['insertionSort'] for r in results]
    mergeTimes = [r['mergeSort'] for r in results]

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, insertionTimes, marker='o', label='Insertion Sort', linewidth=2)
    plt.plot(sizes, mergeTimes, marker='s', label='Merge Sort', linewidth=2)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Time Comparison: Insertion Sort vs Merge Sort')
    plt.legend()
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig('sorting_algorithms_comparison.png', dpi=300)
    plt.show()
    print("\n✓ Plot saved as 'sorting_algorithms_comparison.png'")

if __name__ == "__main__":
    main()
