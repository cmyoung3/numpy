import numpy as np
import random
#each set of brackets is a row. So we have two rows with three columns in each (row 1 is 123 row 2 is 456)
array01 = np.array([[1,2,3],
                    [4,5,6]])

array02 = np.array([0.0, 0.1, 0.2, 0.3, 0.4])

for row in array01:
    print(row)
    for col in row:
        print(col, end=' ')
    print()


for i in array01.flat:
    print(i)

array03 = np.zeros(5)

array04 = np.ones((2,4), dtype=int)

array05 = np.full((3,5),13)

#exercise
a = np.array([[random.randint(1,10) for i in range(5)],[random.randint(1,10) for i in range(5)]])

b  = np.array(np.random.randint(1,10,size=(2,5)))

array06 = np.arange(5)

array07 = np.arange(5,10)

array08 = np.arange(10,1,-2)

print()

