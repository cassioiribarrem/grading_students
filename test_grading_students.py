from unittest import TestCase
from main import Grading_students

class TestGradingStudents():
    def tests_if_grading_students_exists(self):
        if Grading_students([38, 19, 79, 34, 62]):
            return

    def tests_if_grading_students_is_recieving_parameters(self):
        assert result.grades == [38, 19, 79, 34, 62]

    def tests_rounding_existence(self):
        if result.rounding():
            return

    def tests_rounding_output(self):
        assert result.rounding() == [40, 19, 80, 34, 62]



result = Grading_students([38, 19, 79, 34, 62])