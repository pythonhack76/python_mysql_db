import numpy as np  
import warnings

#gestione degli avvisi per non printare
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 

#esempio di array
arr = np.array([1,2,3,4,5])

lista = [1,2,3,4,5,6]

#zero
arr = np.array(42)

#one
arr1 = np.array([1,2,3,4,5], dtype=object, ndmin=5)

#two
arr2 = np.array([[1,2,3,4,5],
                    [6,7,8,9]])

#three

arr3 = np.array([ 
                [[1,2,3,4,5],[5,6,7,8],
                [2,3,2,3,2,3],[10,11,12]] ])

#creazione di un range di dati - ultimo valore lo stacco
arrRange = np.arange(5,70,9)

arrZeros = np.zeros((3,2,1))



print(arrZeros)


