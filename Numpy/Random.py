import numpy as np   
from numpy import array, random, size

import warnings

#gestione degli avvisi per non printare
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 

values = np.array([10, 23, 21, 43, 54])

#arr = random.randint(100, size=(15,4))
probability = np.array([0.1, 0.2, 0.2, 0.3, 0.2])
arrChoice = random.choice(values, p=probability, size=(20))

#random.shuffle(values)

arr2 = random.permutation(values)

#print(arrChoice)
# print(numero)
# print(arr)

print(values)