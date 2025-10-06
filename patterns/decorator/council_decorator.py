__author__ = "Ridham Sood"
__version__ = "1.0.0"

from patterns.decorator.student_decorator import StudentDecorator

class CouncilDecorator(StudentDecorator):
    """
    Decorator to be applied to student objects for students eho 
    participate in the student council. Student who participate in
    student council receive a gpa boost.
    """

    @property
    def grade_point_average(self) -> float:
        """
        Grade Point average accessor 
        Returns:
        float: The value of the grade point average with a boost applied.
        """

        grade_point_average = super().grade_point_average

        increases: dict[float, float] = {
            4.13: .35,
            3.66: .19,
            2.4: .03 
        }
        increase = 0
        for average in increases:
            if grade_point_average >= average:
                increase = increases[average]
                break
        return grade_point_average + increase
