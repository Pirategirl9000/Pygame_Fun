"""
Class for navigating a matrix based map
"""
from abc import abstractmethod
import numpy as np

class Matrixical_Navigation(object):
    @abstractmethod
    def move(self, direction:str, matrix:any, value:any = 1):
        pass
    @abstractmethod
    def get_loc(self, matrix, value):
        pass
    
    @abstractmethod  
    def __canMove(self, player_loc, direction, matrix):
        pass
        
        
class List_nav(object, Matrixical_Navigation):
    def __init__(self, matrix:list):
        self.matrix = matrix
    
    def move(self, direction:str, value:any = 1):
        """
        Moves actor through a matrix
        *args: str direction("w", "a", "s", "d", "up", "left", "right", "down"), any[] matrix
        args: str direction, any value
        return: any[] matrix
        """
        
        player = self.get_loc(value)
        
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
            store = self.matrix[player[0]][player[1]-1]
            self.matrix[player[0]][player[1]-1] = value
            self.matrix[player[0]][player[1]] = store
            return self.matrix
        elif (direction == "right" and player[1] != len(self.matrix[player[0]]) - 1):
            store = self.matrix[player[0]][player[1]+1]
            self.matrix[player[0]][player[1]+1] = value
            self.matrix[player[0]][player[1]] = store
            return self.matrix
        elif (direction == "up" and player[0] != 0 and self.__canMove(player, direction)):
            store = self.matrix[player[0]-1][player[1]]
            self.matrix[player[0]-1][player[1]] = value
            self.matrix[player[0]][player[1]] = store
            return self.matrix
        elif (direction == "down" and player[0] != len(self.matrix) - 1 and self.__canMove(player, direction)):
            store = self.matrix[player[0]+1][player[1]]
            self.matrix[player[0]+1][player[1]] = value
            self.matrix[player[0]][player[1]] = store
            return self.matrix
        else:
            return self.matrix
        
    def get_loc(self, value:any = 1):
        """
        Gets (y,x) index of the actor
        *args: any[] matrix, any value
        returns: [int y_ind, int x_ind]
        """
        for row in self.matrix:
            for item in row:
                if item == value:
                    return [self.matrix.index(row), row.index(item)]
                
        return ValueError(f"The Value: {value} Was Not Found Within the Matrix")
                
    def __canMove(self, player_loc:list, direction:str):
        """
        Determines whether actor can move up or down along a matrix
        *args: int[] player_loc, str direction, any[] matrix
        return: bool canMove
        """
        row_length = 0
        if (direction == "up"):
            row_length = len(self.matrix[player_loc[0] - 1])
        elif (direction == "down"):
            row_length = len(self.matrix[player_loc[0] + 1])
            
        if (player_loc[1] < row_length):
            return True
        else:
            return False    
  
class Np_array_nav(object, Matrixical_Navigation, np):
    def __init__(self, matrix:np.ndarray):
        self.matrix = matrix
    
    
    def move(self, direction:str, value:any = 1):
        """
        Moves actor through a matrix
        *args: str direction("w", "a", "s", "d", "up", "left", "right", "down")
        args: str direction, any value
        return: np.ndarray matrix
        """
        
        player = self.get_loc(value)
        
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
            store = self.matrix[player[0], player[1]-1]
            self.matrix[player[0], player[1]-1] = value
            self.matrix[player[0], player[1]] = store
            return self.matrix
        elif (direction == "right" and player[1] != len(self.matrix[player[0]]) - 1):
            store = self.matrix[player[0], player[1]+1]
            self.matrix[player[0], player[1]+1] = value
            self.matrix[player[0], player[1]] = store
            return self.matrix
        elif (direction == "up" and player[0] != 0 and self.__canMove(player, direction)):
            store = self.matrix[player[0]-1, player[1]]
            self.matrix[player[0]-1, player[1]] = value
            self.matrix[player[0], player[1]] = store
            return self.matrix
        elif (direction == "down" and player[0] != len(self.matrix) - 1 and self.__canMove(player, direction)):
            store = self.matrix[player[0]+1, player[1]]
            self.matrix[player[0]+1, player[1]] = value
            self.matrix[player[0], player[1]] = store
            return self.matrix
        else:
            return self.matrix
        
    def get_loc(self, value:any):
        """
        Gets (y,x) index of the actor
        *args: any value
        returns: [int y_ind, int x_ind]
        """
        #used i and j so I don't need to learn numpy indexing with for loops
        i = 0
        j = 0
        
        for row in self.matrix:
            for item in row:
                if item == value:
                    return [i, j] #(y, x)
                j += 1
            i += 1
        
        return ValueError(f"The Value: {value} Was Not Found Within the Matrix")
                
    def __canMove(self, player_loc, direction):
        """
        Determines whether actor can move up or down along a matrix
        *args: int[] player_loc, str direction
        return: bool canMove
        """
        row_length = 0
        if (direction == "up"):
            row_length = len(self.matrix[player_loc[0] - 1])
        elif (direction == "down"):
            row_length = len(self.matrix[player_loc[0] + 1])
            
        if (player_loc[1] < row_length):
            return True
        else:
            return False