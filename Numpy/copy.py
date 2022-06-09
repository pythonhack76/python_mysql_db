import numpy as np   

import warnings

#gestione degli avvisi per non printare
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 

arr = np.array([1,2,3,4])

arrCopy = arr.view()
arr[0] = 10
print(arr)
print(arr.base)
print(arrCopy)
print(arrCopy.base)