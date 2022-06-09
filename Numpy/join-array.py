import numpy as np   

import warnings

#gestione degli avvisi per non printare
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 

# arr1 = np.array([[1,2],[3,4]])
# arr2 = np.array([[5,6],[7,8]])
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

#arrConc = np.concatenate((arr1, arr2), axis=1)
arrStack = np.hstack((arr1,arr2))

# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)

#print(arrConc)
print(arrStack)
