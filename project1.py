import numpy as np


def pivot(A, nrows):
    pivotCols = []
    A_t = np.transpose(A)
    I = np.identity(nrows)
    for i in range(0, ncols):
        for j in range(0,nrows):
            if (A_t[i][:] == I[:][j] ).all():

                A[[i, j]] = A[[j, i]]
    identity = np.identity(nrows)

    for i in range(0, nrows):

        if (A_t[i][:] == identity[:][i]).all():
            pivotCols.append(i)
    return pivotCols


def ans(A):
    nrows = np.shape(A)[0]
    ncols = np.shape(A)[1]
    A_t = np.transpose(A)

    if isConsistent(A, nrows, ncols):
        print("consistent")
        pivotCols = pivot(A, nrows)
        print("pivot columns:{} ".format(pivotCols))
        if len(pivotCols) == ncols - 1:
            print("Unique solution")

            print("x=\n{}".format(np.reshape(A_t[ncols - 1][:], (nrows, 1))))

        else:
            print("inf solutions")
            cols = np.arange(0, ncols - 1, 1)
            freeCols = list(set(cols) - set(pivotCols))

            for i in freeCols:
                x = [0] * (ncols - 1)

                for j in range(0, nrows):
                    if A[j][i] != 0:
                        x[j] = -1 * A[j][i]

                x[i] = 1

                print("{}*x{}".format(np.reshape(x, (ncols - 1, 1)), i + 1))

                print("+")

            x = [0] * (ncols - 1)
            for j in range(0, nrows):
                x[j] = A[j][ncols - 1]

            print(np.reshape(x, (ncols - 1, 1)))


    else:
        print("inconsistent")


def isConsistent(A, nrows, ncols):
    A = np.array(A, dtype=np.float64)

    for i in range(0, ncols - 1):
        if A[nrows - 1][i] != 0:
            return True
    if A[nrows - 1][ncols - 1] == 0:
        return True
    else:
        return False



def rref(A):

    nrows = np.shape(A)[0]
    ncols = np.shape(A)[1]

    A = np.array(A, dtype=np.float64)

    lead = 0

    while lead < nrows:

        for r in range(0, nrows):
            d = A[lead][lead]
            if A[lead][lead] != 0:
                m = A[r][lead] / A[lead][lead]

            for c in range(0, ncols):
                if r == lead:
                    if d != 0:
                        A[r][c] /= d
                else:
                    A[r][c] -= A[lead][c] * m
                if A[r][c] == -0:
                    A[r][c] = 0

        lead += 1

        print(A)

        print("******************")





    return A


while True:
    try:
        M = np.matrix(input("Enter coefficient matrix\n"))
        break
    except:
        print("Wrong input for matrix\n the format of input sholud be like:\n\t1,2,3;4,5,6 \nor [1,2,3;4,5,6]")
        continue

row = np.shape(M)[0]

print("Enter elements of constant matrix:\n")
const_array = []
for i in range(0, row):
    n = input("enter element of row #{} :".format(i + 1))
    const_array.append(int(n))

M = np.c_[M, const_array]

print(M)
print("************start************")
M_rref = rref(M)
print(M_rref)
nrows = np.shape(M_rref)[0]
ncols = np.shape(M_rref)[1]
ans(M_rref)

# example of input:
#  Enter elements of constant matrix:
# 1,3,2,-4,3;-2,-1,2,6,4;0,-1,3,-5,1;3,-4,2,5,-7;1,2,-8,6,1


# enter element of row #1 :-3
# enter element of row #2 :19
# enter element of row #3 :-2
# enter element of row #4 :-11
# enter element of row #5 :4
