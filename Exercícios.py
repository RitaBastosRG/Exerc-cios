from operator import itemgetter
from itertools import groupby, islice
from decimal import Decimal
python_list = []
scores_list = []
sorted_list = []
N = int(input("Enter number of students between 2 and 5, inclusive "))

for ii in range(N):
    name = (str(input("Enter student name ")))
    score = (float(input("Enter grade of student ")))
    python_list.append([name, score])


def Sort(sub_li):
    sub_li.sort(key=lambda x: x[1])
    return sub_li


sorted_list = Sort(python_list)

second_grade = sorted_list[1][1]
for ii in range(len(sorted_list)):
    if sorted_list[ii][1] == second_grade:
        scores_list.append(sorted_list[ii])
        alfa_list = sorted(scores_list)

for x in range(len(alfa_list)):
    print(alfa_list[x][0])

# código bom

a = []
for i in range(int(input())):
    x, y = (input(), Decimal(input()))
    a.append((y, x))
a.sort()
for k, v in islice(groupby(a, key=itemgetter(0)), 1, 2):
    for x in v:
        print(x[1])

#outro código
n = int(input())
l = []
grade = []
for i in range(n):
    name = input()
    score = float(input()) 
    l.append([name,score])
    grade.append(score)
grade = sorted(set(grade))
second_lowest = grade [1]
names = []
for val in l:
    if second_lowest == val[1]:
        names.append(val[0])
names.sort()
for nm in names:
    print(nm)
