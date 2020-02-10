# -*- coding: utf-8 -*-
import numpy as np
a=np.array([[3,6,2],[3,2,4],[1,3,4]])
print(a)




#another code
print(" ")

import numpy as np
s=np.array([[1,3,5],[1,6,3],[7,6,5]])
print(s)


print(" ")

import numpy as np
k=np.array([[12,13,14,15],[20,21,22,23],[10,20,30,40]])
print(k)

print(" ")

import numpy as np
d=np.array([[10,20,30],[20,40,50],[12,30,43]], dtype=complex)
print(d)

print("1 ..")
print(" ")

import numpy as np
ra=np.array([[1,3,2,4],[5,4,3,4],[1,7,4,9]],dtype=int)
print(ra)
print(" ")
print(ra.size)
print(" ")
print(ra.shape)
print(" ")
print(ra.reshape(4,3))
print(" ")
print(np.power(ra,2))

print(" ")
print("new:1")



import numpy as np
sort=np.array([[19,42,33,14],[50,26,17,38],[11,23,25,47]])
quicksort=np.sort(sort,axis=1,kind='quicksort',order=None)
marge=np.sort(sort,axis=1,kind='margesort',order=None)
#print(quicksort)
#print(marge)















