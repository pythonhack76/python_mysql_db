import numpy as np   

import warnings

#gestione degli avvisi per non printare
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 


arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#arr = np.array([[1,2,3],[4,5,6]])

#print(arr.shape)


#print(arr.reshape(-1))

print(arr.reshape(4,3))