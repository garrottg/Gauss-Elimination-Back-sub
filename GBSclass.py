## We will make the GBS code using OOP now.
import numpy as np
import sys

class GaussElimination():
    p_int = None
    #Get the augmented matrix
    def AM(self, A, b):
        self.size = len(b)
        for i in range(0, self.size):
            A[i].append(b[i])
        self.matrix = np.array(A, dtype = "float64")
        return self.matrix

    #Get the Augmented matrix in reduced/triangular form
    def AM_rf(self):
        for i in range(0, self.size-1):
            for p in range(i, self.size):
                if self.matrix[p][i] != 0:
                    p_int = p
                    break

            if p_int is None:
                print("no unique solution exists")
                sys.exit()

            #This swithces a row if it starts with zero.
            if p_int != i:
                self.matrix[[i, p_int]] = self.matrix[[p_int, i]]

            #row transformation
            for j in range(i+1, self.size):
                mij = self.matrix[j][i]/self.matrix[i][i]
                self.matrix[j] = self.matrix[j] - mij*self.matrix[i]
        return self.matrix
    
    #Get the xvalues
    def x_values(self):
        if self.matrix[self.size-1][self.size-1] == 0:
            print("no unique solution exists")
            sys.exit()

        x = [0*i for i in range(0,self.size)]
        x[self.size-1] = self.matrix[self.size-1][self.size]/self.matrix[self.size-1][self.size-1]

        for i in reversed(range(0, self.size-1)):
            sum = 0
            for j in range(i+1, self.size):
                sum += self.matrix[i][j]*x[j]
                x[i] = (self.matrix[i][self.size] - sum)/self.matrix[i][i]

        return x
    
#Example
A = [[1,-1,2,-1],[2,-2,3,-3],[1,1,1,0],[1,-1,4,3]]
b = [-8, -20, -2, 4]

gauss = GaussElimination()
print(gauss.AM(A = A, b = b))
print(gauss.AM_rf())
print(gauss.x_values())