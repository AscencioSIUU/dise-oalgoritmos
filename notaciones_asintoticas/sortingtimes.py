import random
from time import perf_counter # requiere python >= 3.3
from insertionsort import * 
from mergesort import *

A = random.sample(range(1000),1000)
B = random.sample(range(1000),10)

result1=list(A)
result2=list(A)
result3=list(B)
result4=list(B)

print ("Con 1000 numeros, el arreglo es: " + str(A))
t1=perf_counter()
insertion_sort(result1)
t2=perf_counter()
print ("\nEl tiempo de insertion fue de: " + str(t2-t1))
t3=perf_counter()
merge_sort(result2, 0, len(result2)-1)
t4=perf_counter()
print ("\nEl tiempo de merge fue de: " + str(t4-t3))

print ("\nCon 10 numeros, el arreglo es: " + str(B))
t5=perf_counter()
insertion_sort(result3)
t6=perf_counter()
print ("\nEl tiempo de insertion fue de: " + str(t6-t5))
t7=perf_counter()
merge_sort(result4, 0, len(result4)-1)
t8=perf_counter()
print ("\nEl tiempo merge fue de: " + str(t8-t7))

