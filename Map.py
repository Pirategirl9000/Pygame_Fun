"""
Module used for creating and getting a matrixical map from an image
"""

import numpy as np
from skimage import io

class Map(object):
    def __init__(self, file_name:str, binary:bool = False, alpha:bool = False):
        """
        Creates a new map from an image
        args: str file_name, bool binary, bool alpha
        *args: str file_name
        return: None
        """
        im = io.imread(file_name) #RGBA format
        self.imarr = np.array(im)

        #remove alpha
        if not alpha:
            self.imarr = self.imarr[ :, :, 0]

        #change to binary for grayscale and less memory
        if binary:
            self.imarr[self.imarr < 128] = 0
            self.imarr[self.imarr >= 128] = 1
    def get_map(self):
        """
        Returns Map Matrix
        args: None
        *args: None
        return: numpy.array(int[])
        """
        return self.imarr