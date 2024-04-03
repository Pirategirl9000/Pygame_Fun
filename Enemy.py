"""
EnemyObject and associated methods
"""

class Enemy(object):
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
        pass
    
    def move_towards(self, x:int, y:int):
        """
        Enemy moves towards location
        *args: int x, int y
        args: int x, int y
        return: None
        """
        
        # TODO implement move_towards method
    