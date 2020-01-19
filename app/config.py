
from os.path import dirname
from os.path import join
from os.path import realpath
 

class Config:
    """
    Class holds all config files for the application.
    """
    def __init__(self):
        super().__init__()
        self.threshold_value = 250
        self.minimum_distance = 40
        self.alteration_tag = False
        self.rearrangement_tag = False
