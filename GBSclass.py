## We will make the GBS code using OOP now.
import numpy as np

class GaussElimination():
    p_int = None

    def __init__(self, size, matrix):
        self.size = size
        self.matrix = matrix
    
    def AM(self):
        for i in range(0, self.size-1):
            for p in range(i, self.size+1):
                if self.matrix[p][i] != 0:
                    p_int = p
                    break

            if p_int is None:
                print("no unique solution exists")
                break          

            if p_int != i:
                self.matrix[[i, p_int]] = self.matrix[[p_int, i]]

            for j in range(i+1, self.size):
                mij = self.matrix[j][i]/self.matrix[i][i]
                self.matrix[j] = self.matrix[j] - mij*self.matrix[i]
        return self.matrix
    
    def x_values(self):
        if self.matrix[self.size-1][self.size-1] == 0:
            print("no unique solution exists")

        x = [0*i for i in range(0,self.size)]
        x[self.size-1] = self.matrix[self.size-1][self.size]/self.matrix[self.size-1][self.size-1]

        for i in reversed(range(0, self.size-1)):
            sum = 0
            for j in range(i+1, self.size):
                sum += self.matrix[i][j]*x[j]
                x[i] = (self.matrix[i][self.size] - sum)/self.matrix[i][i]

        return x

    
#Example
array = np.array([[1,-1,2,-1,-8],[2,-2,3,-3,-20],[1,1,1,0,-2],[1,-1,4,3,4]], dtype = 'float64')

gauss = GaussElimination(size = 4, matrix = array)
print(gauss.AM())
print(gauss.x_values())