__author__ = "Ridham Sood"
__version__ = "1.0.0"

from enum import Enum, auto

class Department(Enum):
    """
    An enumeration listing each of the departments
    in a school.
    To use:  Department.DEPARTMENT_NAME  
    Example: Department.MEDICINE
    """
    COMPUTER_SCIENCE = auto() # COMPUTER_sCIENCE = 1
    EDUCATION = auto() # EDUCATION = 2
    ENGINEERING = auto()
    MEDICINE = auto()


    
