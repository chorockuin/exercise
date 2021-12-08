def _41():
    class ToDicMixin:
        def to_dict(self):
            return self._traverse_dict(self.__dict__)

        def _traverse_dict(self, inst_dict):
            output = {}
            for k, v in inst_dict.items():
                output[k] = self._traverse(k, v)
            return output

        def _traverse(self, k, v):
            if isinstance(v, ToDicMixin):
                return v.to_dict()
            elif isinstance(v, dict):
                return self._traverse_dict(v)
            elif isinstance(v, list):
                return [self._traverse(k, i) for i in v]
            elif hasattr(v, '__dict__'):
                return self._traverse_dict(v.__dict__)
            else:
                return v

def _42():
    class A:
        def __init__(self):
            self.public_var = 1
            self._protected_var = 2
            self.__private_var = 3
            print(self.public_var, self._protected_var, self.__private_var)
    
    class B(A):
        def access(self):
            print(self.__dict__)
            print(self.public_var, self._protected_var, self.__private_var)

    b = B()
    b.access()

from weakref import WeakKeyDictionary
def _46():
    class Homework:
        def __init__(self):
            self._grade = 0

        @property
        def grade(self):
            return self._grade

        @grade.setter
        def grade(self, value):
            if not (0 <= value <= 100):
                raise ValueError('점수는 0과 100 사이입니다')
            self._grade = value

    galileo = Homework()
    galileo.grade = 100
    print(galileo.grade)

    class Grade:
        def __init__(self):
            self._values = WeakKeyDictionary()

        def __get__(self, instance, instance_type):
            if instance is None:
                return self
            return self._values.get(instance, 0)

        def __set__(self, instance, value):
            if not (0 <= value <= 100):
                raise ValueError('점수는 0과 100 사이입니다')
            self._values[instance] = value

    class Exam:
        math_grade = Grade()
        writing_grade = Grade()
        science_grade = Grade()

    exam = Exam()
    exam.writing_grade = 40
    print(exam.writing_grade)

    exam2 = Exam()
    exam2.writing_grade = 80
    print(exam2.writing_grade)

_46()
# _42()
# _41()
