import numpy as np   

import warnings

#gestione degli avvisi per non printare
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 


# arr = np.array([1,2,3,4,5,6])

# arr2d = np.array([[1,2], [3,4],[5,6],[7,8],[9,10],[11,12]])

# arr2 = np.array_split(arr2d, 4, axis=1 )

# print(arr2)

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])

arr2 = np.hsplit(arr,1)

print(arr2)