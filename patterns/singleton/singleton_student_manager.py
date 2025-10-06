__author__ = "Ridham Sood"
__version__ = "1.0.0"

class SingletonStudentManager:
    """
    SingletonStudentManage: Employs the singleton pattern to ensure only
    one instance of the class is in memory at a time.
    """
    __instance__ = None
    __next_student_number__ = 20240000

    def __new__(cls):
        """COnstructs the SingletonStudent instance but only if it does
        not already exist in the memory.
        """
        if not cls.__instance__:
            # Create new instance
            cls.__instance__ = super(SingletonStudentManager, cls).__new__(cls)
        
        return cls.__instance__
    
    def get_next_student_number(self) -> int:
        """Returns the next student number and increments the 
        internal counter."""

        student_number = self.__next_student_number__
        self.__next_student_number__ += 1
        return student_number