class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        MODIFIED = -1000000
        R = len(matrix)
        C = len(matrix[0])
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    # We modify the elements in place. Note, we only change the non zeros to MODIFIED
                    for k in range(C):
                        matrix[r][k] = MODIFIED if matrix[r][k] != 0 else 0
                    for k in range(R):
                        matrix[k][c] = MODIFIED if matrix[k][c] != 0 else 0
        for r in range(R):
            for c in range(C):
                # Make a second pass and change all MODIFIED elements to 0 """
                if matrix[r][c] == MODIFIED:
                    matrix[r][c] = 0

'''Not effecient:
Time Complexity : O((M * N)* (M + N))
Space Complexity : O(1)'''

class Solution1(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        is_col=False
        row=len(matrix)
        column=len(matrix[0])

        for i in range(row):

            if matrix[i][0]==0:
                is_col=True
            for j in range(1, column):
                    if matrix[i][j]==0:
                        matrix[0][j]=0
                        matrix[i][0]=0
                        
        for i in range(1, row):
            for j in range(1, column): 
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j]=0
        
        if matrix[0][0]==0:
            for j in range(column):    
                matrix[0][j]=0

        if is_col:
            for i in range(row):
                matrix[i][0]=0  

'''  Time Complexity : O((M * N)
Space Complexity : O(1)'''                            
