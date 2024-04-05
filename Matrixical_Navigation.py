"""
Class for navigating a matrix based map
"""
class Matrixical_Navigation(object):
    def move(self, direction:str, matrix:list, value:any = 1, square:bool = True):
        """
        Moves actor through a matrix
        *args: direction:str("w", "a", "s", "d", "up", "left", "right", "down"), matrix:int[]
        args: direction:str, matrix:int[], value:any square_matrix:bool
        return: matrix = int[list]
        """
        player = self._get_loc(matrix, value)
        
        if direction == "a":
            direction = "left"
        elif direction == "s":
            direction = "down"
        elif direction == "w":
            direction = "up"
        elif direction == "d":
            direction = "right"
        else:
            raise ValueError("Invalid Movement Direction Was Passed")
            
            
        
        if (direction == "left" and player[1] != 0):
            store = matrix[player[0]][player[1]-1]
            matrix[player[0]][player[1]-1] = value
            matrix[player[0]][player[1]] = store
            return matrix
        elif (direction == "right" and player[1] != len(matrix[player[0]]) - 1):
            store = matrix[player[0]][player[1]+1]
            matrix[player[0]][player[1]+1] = value
            matrix[player[0]][player[1]] = store
            return matrix
        elif (direction == "up" and player[0] != 0):
            store = matrix[player[0]-1][player[1]]
            matrix[player[0]-1][player[1]] = value
            matrix[player[0]][player[1]] = store
            return matrix
        elif (direction == "down" and player[0] != len(matrix) - 1):
            store = matrix[player[0]+1][player[1]]
            matrix[player[0]+1][player[1]] = value
            matrix[player[0]][player[1]] = store
            return matrix
        else:
            return matrix
        
    def _get_loc(self, matrix, value):
        """
        Gets (y,x) index of the actor
        *args: matrix:int[], value:any
        returns: [y_ind:int, x_ind:int]
        """
        for row in matrix:
            for item in row:
                if item == value:
                    return [matrix.index(row), row.index(item)]