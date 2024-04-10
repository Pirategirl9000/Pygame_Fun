"""
Module used for creating and getting a matrixical map from an image
"""

import numpy as np
import math
from skimage import io

class Map(object):
    def __init__(self, file_name:str, binary:bool = False, alpha:bool = False, grey_scale:bool = False, binary_dark_value:any = 0, binary_light_value:any = 1):
        """
        Creates a new map from an image
        args: str file_name, bool binary, bool alpha, bool grey_scale, any binary_dark_value, any binary_light_value
        *args: str file_name
        return: None
        """
        try:
            im = io.imread(file_name) #RGBA format
        except FileNotFoundError:
            raise ValueError(f"File: {file_name} Could Not be Found")
        self.imarr = np.array(im)

        #remove alpha
        if not alpha:
            self.imarr = self.imarr[ :, :, 0:3] #RGB format
            
        if grey_scale: #mono removes alpha
            self.imarr = math.floor((self.imarr[ :, :, 0] + self.imarr[ :, :, 1] + self.imarr[ :, :, 2]) / 3)
            
        if binary:
            self.imarr[self.imarr < 128] = binary_dark_value
            self.imarr[self.imarr >= 128] = binary_light_value
    def get_map(self):
        """
        Returns Map Matrix
        args: None
        *args: None
        return: np.ndarray matrix_map
        """
        return self.imarr