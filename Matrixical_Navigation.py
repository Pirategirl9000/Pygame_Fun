"""
Class for navigating a matrix based map
"""
class Matrixical_Navigation(object): 
    def move(self, direction:str, matrix:list, value:any = 1):
        """
        Moves actor through a matrix
        *args: direction:str("w", "a", "s", "d", "up", "left", "right", "down"), matrix:list
        args: direction:str, matrix:list, value:any
        return: matrix:list
        """
        
        #TODO Change to use numpy arrays as well
        
        player = self.__get_loc(matrix, value)
        
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
        elif (direction == "up" and player[0] != 0 and self.__canMove(player, direction, matrix)):
            store = matrix[player[0]-1][player[1]]
            matrix[player[0]-1][player[1]] = value
            matrix[player[0]][player[1]] = store
            return matrix
        elif (direction == "down" and player[0] != len(matrix) - 1 and self.__canMove(player, direction, matrix)):
            store = matrix[player[0]+1][player[1]]
            matrix[player[0]+1][player[1]] = value
            matrix[player[0]][player[1]] = store
            return matrix
        else:
            return matrix
        
    def __get_loc(self, matrix, value):
        """
        Gets (y,x) index of the actor
        *args: matrix:list, value:any
        returns: [y_ind:int, x_ind:int]
        """
        for row in matrix:
            for item in row:
                if item == value:
                    return [matrix.index(row), row.index(item)]
                
    def __canMove(self, player_loc, direction, matrix):
        """
        Determines whether actor can move up or down along a matrix
        *args: player_loc:int[], direction:str, matrix:list
        return: canMove:bool
        """
        row_length = 0
        if (direction == "up"):
            row_length = len(matrix[player_loc[0] - 1])
        elif (direction == "down"):
            row_length = len(matrix[player_loc[0] + 1])
            
        if (player_loc[1] < row_length):
            return True
        else:
            return False