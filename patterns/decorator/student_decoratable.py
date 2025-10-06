__author__ = "Ridham Sood"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class StudentDecoratable(ABC):

    """
    Interface ti be applied the Student class.
    Note: Add more abstract methods to support future decorators as
    needed.
    """

    @abstractmethod
    def grade_point_average(self) -> float:
        pass
                            