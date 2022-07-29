class Student:
    def __init__(self, name, age, gender, subjects, total_score):
        self.name = name
        self.age = age
        self.gender = gender
        self.subjects = subjects
        self.total_score = total_score

def print(self):
    return self.__dict__