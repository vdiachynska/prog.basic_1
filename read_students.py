import pickle
with open("student_dict.txt", "rb") as file:
    data1 = pickle.load(file)
for i in data1:
    print(i + ':')
    for j in data1[i]:
        print('\t' + j + ':' + '\n' + 2 * '\t', end='')
        print(*data1[i][j], sep='\n' + 2 * '\t')
    print()