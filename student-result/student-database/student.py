import pymongo
from helper import search
from model import Student
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydata = myclient["mydatabase"]

mycollection = mydata["customers"]

def find():
    name = input("Enter name of student: ")
    student_exist = mycollection.find_one({"name": name})
    if student_exist:
        print("student record")
    else:
        print("failure message")


def register():
    subjects = []
    name = input("Enter name of student: ")
    age = int(input("Enter your age here: "))
    gender = input("Enter your gender here: ")
    student_exist = mycollection.find_one({"name": name})
    if student_exist:
        print("failure message")
    else:
        number_of_subjects = 3
        for subject in range(number_of_subjects):
            name_of_subject = input("Enter name of subject: ")
            subjects.append(name_of_subject)

        subject_score = {}
        for m in subjects:
            scores = int(input(f"Enter your score here for {m}: "))
            subject_score[m] = scores
        
        score_list = []
        for n in subject_score.values():
            score_list.append(n)
        total = sum(score_list)
        
        data = Student(name, age, gender, subject_score, total)
        mycollection.insert_one(data)

def update():
    name = input("Enter name of student: ")
    existing_student = search(name)
    if existing_student:
        print(existing_student)