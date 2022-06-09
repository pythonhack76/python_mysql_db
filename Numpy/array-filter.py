import numpy as np   

import warnings

#gestione degli avvisi per non printare
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 

arr = np.array([0,1,2,3,4,5,6,7,8])

arr_testo = np.array(["pippo","giovanni","enzo","matteo"])

arrIndici = np.where(arr%2 == 0)

arrOrdinato = np.sort(arr_testo)


#creazione filtro dinamico 
filtro = []
for numero in arr:
    if numero%2 == 0:
        filtro.append(True)
    else:
        filtro.append(False)

arrayFiltrato = arr[filtro]


#shortcode
filtro2 = arr%2 == 0
arrayFiltrato2 = arr[filtro2]

print(arrayFiltrato)

print(arrayFiltrato2)

# print(arrIndici)

# print(arrOrdinato)

