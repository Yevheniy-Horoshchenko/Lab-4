import numpy as np
#1
print("Task:1\n---------")
A = np.matrix([[1,2],[4,-1]])
B = np.matrix([[2,-3],[-4,1]])
C = A*B - B*A
print(C)
#2
print("Task:2\n---------")
m = np.matrix([[-1,2],[0,1]])
result = np.linalg.matrix_power(m,2)
print(result)
#3
print("Task:3\n---------")
A = np.matrix([[5,8,-4],[6,9,-5],[4,7,-3]])
B = np.matrix([[3,2,5],[4,-1,3],[9,6,5]])
C = A.dot(B)
print(C)
#4
print("Task:4\n---------")
m = np.matrix([[2,4,5],[1,1,2],[2,4,3]])
print(m)
print(m.T)
det_m = round(np.linalg.det(m),3)
det_m_t = round(np.linalg.det(m.T),3)
print(det_m)
print(det_m_t)
#5
print("Task:5\n---------")
m = np.matrix([[1,2,3,4],[-2,1,-4,3],[3,-4,-1,2],[4,3,-2,-1]])
print(m)
print(m.T)
det_m = round(np.linalg.det(m),3)
det_m_t = round(np.linalg.det(m.T),3)
print(det_m)
print(det_m_t)