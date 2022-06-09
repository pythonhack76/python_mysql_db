import numpy as np   

import warnings

#gestione degli avvisi per non printare
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 


arr = np.array([1,2,3,4,5])

# arr2 = np.array(["1","12","32"], dtype='i')
arr2 = np.array(["1","12","32"])

print(arr.dtype)

arrInt = arr.astype(int)
print(arrInt+4)
