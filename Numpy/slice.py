import numpy as np  
import warnings

#gestione degli avvisi per non printare
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 


arr = np.array(["asb","qwe","we",3,"er"])
arr2 = np.arange(12)


arr2d = np.array([[0,1,2], [4,5,6]])
arr3d = np.array([[[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10]], [[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10]]])

print(arr3d[0,0::2])


