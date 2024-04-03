"""
EnemyObject and associated methods
"""
import Game

class Enemy(object, Game):
    def __init__(self, x:int, y:int):
        """
        Create new Enemy Object
        *args: int x, int y
        args: int x, int y
        return: None
        """
        self.x = x
        self.y = y
        self.alive = True
        
        self.__search() #starts seeking out player
        pass
    
    def move_towards(self, x:int, y:int):
        """
        Enemy moves towards location
        *args: int x, int y
        args: int x, int y
        return: None
        """
        
        # TODO implement move_towards method
        
    def __search(self):
        """
        Enemy begins searching for player using search algorithm
        *args: None
        args: None
        return: None
        """
        pass
    
    def __chase(self):
        """
        Enemy sees player and attempts to kill them
        *args: None
        args: None
        return: None
        """
        
        pass
    def __hit_player(self):
        pass