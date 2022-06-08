import numpy as np   

import warnings

#gestione degli avvisi per non printare
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 

arr1D = np.array([1,2,3,4,5])
arr2D = np.array([[1,2,3],
                    [4,5,6]])
arr3D = np.array([  [[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]] ])

print(arr2D[1,1])

print(arr3D[1,1,0])


