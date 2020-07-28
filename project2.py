import numpy as np
import sympy


def nulA(A, pivotCols):
    nrows = np.shape(A)[0]
    ncols = np.shape(A)[1]
    A = np.array(A, dtype=np.float64)
    A_t = np.transpose(A)
    print("pivot columns: {}".format(pivotCols))
    if len(pivotCols) == ncols - 1:
        print("x=[[x1]\n  [x2]\n  [x3]]=\n{}".format(np.reshape(A_t[ncols - 1][:], (nrows, 1))))
        return 0



    else:

        cols = np.arange(0, ncols - 1, 1)
        freeCols = list(set(cols) - set(pivotCols))

        for i in freeCols:
            x = [0] * (ncols - 1)

            for j in range(0, nrows):

                if A[j][i] != 0:
                    x[j] = -1 * A[j][i]

            x[i] = 1

            print("{}*x{}".format(np.reshape(x, (ncols - 1, 1)), i + 1))
            if i < max(freeCols):
                print("+")
        return len(freeCols)


while True:
    try:
        M = np.matrix(input("Enter coefficient matrix A:\n"))
        break
    except:
        print("Wrong input for matrix\n the format of input sholud be like:\n\t1,2,3;4,5,6 \nor [1,2,3;4,5,6]")
        continue
nrows = np.shape(M)[0]
ncols = np.shape(M)[1]
const_array = [0] * np.shape(M)[0]
M_null = np.c_[M, const_array]
M_null_rref = sympy.Matrix(M_null).rref()[
    0]  # We can use the rref() method that was used in project1 or sympy.Matrix(M).rref() for reduced echelon form
pivotCols = sympy.Matrix(M_null).rref()[
    1]  # We can use the pivot() method that was used in project1 or sympy.Matrix(M).rref() for pivot columns
M_null_rref = np.reshape(M_null_rref, (nrows, ncols + 1))
print("A = ")
print(M)
print("Augmented matrix of equation Ax=0 : ")
print(M_null_rref)
print("Dimension of nulA:{}".format(nulA(M_null_rref, pivotCols)))
M_rref = sympy.Matrix(M).rref()[0]
M_T = np.transpose(M)
print("Bases of A:\n")
for i in pivotCols:
    print(np.reshape(M_T[i][:], (nrows, 1)), end=",\n")
    print()
print("Rank A is dimension of ColA = {}".format(len(pivotCols)))

# example of input:
# Enter coefficient matrix A:
#  1,3,2,-4,3;-2,-1,2,6,4;0,-1,3,-5,1;3,-4,2,5,-7;1,2,-8,6,1
