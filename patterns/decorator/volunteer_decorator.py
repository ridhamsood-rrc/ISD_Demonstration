__author__ = "Ridham Sood"
__version__ = "1.0.0"

from patterns.decorator.student_decorator import StudentDecorator

class VolunteerDecorator(StudentDecorator):
    """
    Decorator applied to student object for student who participate in
    volunteer activities. Student who volunteer receive gpa boost.
    """

    @property
    def grade_point_average(self) -> float:
        """
        Grade Point Average accessor.
        
        Returns:
        float: The value of the grade point average with gpa boost applied.
        """

        return super().grade_point_average + .25