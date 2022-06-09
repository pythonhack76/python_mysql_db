import numpy as np   

import warnings

#gestione degli avvisi per non printare
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 


#arr = np.array([[1,2,3],[4,5,6]])

arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

# for x in arr:
#     for y in x:
#         for z in y:
#             print(z)

#flags=['buffered'], op_dtypes=['S']

# for x in np.nditer(arr[:,::2]):
#     print(x)

for index, x in np.ndenumerate(arr):
    print(index, x)
    