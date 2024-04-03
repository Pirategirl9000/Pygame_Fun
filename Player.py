"""
PlayerObject and associated methods
"""

class Player(object):
    def __init__(self):
        """
        Create new Player Object
        *args: None
        args: None
        return: None
        """
        
        self.alive = True
        self.x = 0
        self.y = 200
        
        pass
    
    def getAlive(self):
        """
        Returns whether or not Player is alive
        *args: None
        args: None
        returns: boolean
        """
        return self.alive
    def get_pos(self):
        """
        Returns X and Y coordinates
        *args: None
        args: None
        returns: int[x, y]
        """
        return [self.x, self.y]