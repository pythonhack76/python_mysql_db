import numpy as np   

import warnings

#gestione degli avvisi per non printare
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 

arr = np.array([2,3,4,5,6])
def addCinque(x):
    return x + 5

addCinque = np.frompyfunc(addCinque, 1, 1)

print(addCinque(arr))