"""
3. feladat: Szentpétervári paradoxon
Egy érmével addig dobunk, míg a fej oldalára nem esik. Ha ez az n-edik
feldobáskor történik meg, akkor a játékos 2n forintot nyer (ld. Wikipédia).
Szimuláljunk m játékot (azaz m fej dobásig játszunk). Mennyi a nyeremény átlaga m=100,
m=10000 és m=1000000 esetén?
A program kimenete e három átlag szóközzel elválasztva.
A feladat célja egy végtelen várható értékű valószínűségi változóval való tapasztalatszerzés.
A feladat a példatárban 3.21 sorszámmal szerepel.
"""

import numpy as np
summ=0
my_list = []
eredeti_lista= []

for x in range(100):
    i = 0
    while True:
        if np.random.randint(low=0, high=2, size=1) == 1:
            eredeti_lista.append(i)
            my_list.append(2**i)
            break
        else:
            i += 1

print('Lista hossza:',len(my_list))
for y in range(0, len(my_list)):
    summ = summ + my_list[y]

print('Nyeremények összege: ',summ)
average = summ / len(my_list)

print('Nyeremények átlaga: ',average)
