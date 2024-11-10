from random import randint, choice
import pickle
No = 1
languages = ["Python", "C++", "C#", "Java"]

with open("data.csv", "w") as datafile:
    datafile.write("No, Student, Age, Grade, Sex, Prog. Language\n")
    while No < 201:
        string = f"{No}, student{No}, "
        age = randint(13, 16)
        if age == 13:
            grade = randint(8, 9)
        elif age == 14:
            grade = randint(9, 10)
        elif age == 15:
            grade = randint(10, 11)
        else:
            grade = 11
        sex = choice(["m", "f"])
        language = choice(languages)
        string += f"{age}, {grade}, {sex}, {language}\n"
        datafile.write(string)
        No += 1
    data = []
    groups = {}

with open("data.csv", "r") as file:
    file.readline()  # те саме
    for line in file:
        a = [int(i) if i.isdigit() else i for i in line[:-1].split(', ')]
        data.append(a)
for i in range(8, 12):
    groups[f'{i} grade']={}
    for key in languages:
        groups[f'{i} grade'][key]=[]

for i in range(len(data)):
    gr = str(data[i][3]) + ' grade'
    groups[gr][data[i][5]].append(data[i])

with open("student_dict.txt", "wb") as file:
    pickle.dump(groups, file)



