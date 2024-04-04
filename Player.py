"""
PlayerObject and associated methods
"""
import Game

class Player(object, Game):
    def __init__(self):
        """
        Create new Player Object
        *args: None
        args: None
        return: None
        """
        
        self.alive = True
        
        pass
    
    def get_alive(self):
        """
       Returns whether or not Player is alive
        *args: None
        args: None
        returns: boolean
        """
        return self.alive
    
    def death(self):
        self.alive = False