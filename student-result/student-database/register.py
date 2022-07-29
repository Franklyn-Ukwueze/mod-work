import pymongo 

myclient = pymongo.MongoClient(mongodb)






def register():
    name = input("Enter your name here: ")
    age = int(input("Enter your age here: "))
    gender = input("Enter your gender here: ")
    subjects = []
    number_of_subjects = 3
    for subject in range(number_of_subjects):
        name_of_subject = input("Enter name of subject: ")
        subjects.append(name_of_subject)

    subject_score = {}
    for m in subjects:
        scores = int(input(f"Enter your score here for {m}: "))
        subject_score[m] = scores


    print(subject_score)
        

register()