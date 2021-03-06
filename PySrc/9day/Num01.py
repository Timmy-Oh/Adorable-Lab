# Num01.py
# Array <-- numpy
import numpy as np
d1 = [1,2,'3',4,5]
print(type(d1[1]),type(d1[2]));

a1 = np.array(d1)
print(a1)
print(type(a1),a1.shape, a1.dtype)

d2 = [1,2,3,4,5]
a2 = np.array(d2)
print(a2)
print(type(a2),a2.shape, a2.dtype)

d3 = [[1,2],[3,4],[5,6]]
a3 = np.array(d3)
print(a3)
print(type(a3),a3.shape, a3.dtype)

d4 = [[1,2,3],[4,5,6.0]]
a4 = np.array(d4)
print(a4)
print(type(a4),a4.shape, a4.dtype)

d5 = [[1,2,3],
      [4,5,6,7],
      [8,9]]        # <class 'numpy.ndarray'> (3,) object
a5 = np.array(d5)
print(a5)
print(type(a5),a5.shape, a5.dtype)

d6 = [[1,2,3],
      [4,5,6],
      [7,8,9]]      # <class 'numpy.ndarray'> (3, 3) int32
a6 = np.array(d6)
print(a6)
print(type(a6),a6.shape, a6.dtype)

# d5, d6 --> 2, 6, 8
print(d6[0][1],d6[1][2],d6[2][1])
print(d5[0][1],d5[1][2],d5[2][0])

d7 = [[1,2,3],
      [4,'5',6],
      [7,8,9]]
a7 = np.array(d7)
print(a7)
print(type(a7),a7.shape, a7.dtype)

d8 = [[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]]
a8 = np.array(d8)
print(a8)
print(type(a8),a8.shape, a8.dtype)

# d8 -> 3, 8, 11 출력
print('3, 8, 11 출력')
print(a8[0,1,0], a8[1,1,1], a8[2,1,0])
