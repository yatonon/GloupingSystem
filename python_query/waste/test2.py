from pulp.pulp import LpProblem
from pulp.pulp import LpVariable
from pulp.constants import LpMaximize
from pulp import *

AllStudents = {
    "student1": [53, 63, 65, 63, 94, 42, 58],
    "student2": [13, 53, 69, 24, 42, 19, 48],
    "student3": [40, 7, 10, 82, 64, 86, 2],
    "student4": [51, 19, 36, 75, 92, 92, 14],
    "student5": [73, 82, 22, 29, 72, 74, 77],
    "student6": [73, 82, 22, 29, 72, 74, 77],
}

AllStudentsNumber = {
    "1": [53, 63, 65, 63, 94, 42, 58],
    "2": [13, 53, 69, 24, 42, 19, 48],
    "3": [40, 7, 10, 82, 64, 86, 2],
    "4": [51, 19, 36, 75, 92, 92, 14],
    "5": [73, 82, 22, 29, 72, 74, 77],
    "6": [73, 82, 22, 29, 72, 74, 77],
}

# 今回の問題では総和を最大化するので LpMaximize を指定する
problem = LpProblem('GroupAllScore', LpMaximize)

# 使用する変数
s1 = LpVariable('S1', 1, 6, 'Continuous')
s2 = LpVariable('S2', 1, 6, 'Continuous')
s3 = LpVariable('S3', 1, 6, 'Continuous')
s4 = LpVariable('S4', 1, 6, 'Continuous')
s5 = LpVariable('S5', 1, 6, 'Continuous')
s6 = LpVariable('S6', 1, 6, 'Continuous')
group1 = [s1, s2]
group2 = [s3, s4]
group3 = [s5, s6]
AllStudentsNumberDup = group1 + group2 + group3

# 目的関数
# score1 = AllStudents[group1[0]][0] + AllStudents[group1[1]][1]
# score2 = AllStudents[group2[0]][0] + AllStudents[group2[1]][1]
# score3 = AllStudents[group3[0]][0] + AllStudents[group3[1]][1]
# problem += score1 + score2 + score3

# 制約条件
AllStudentsNumber_keys = [int(n) for n in list(AllStudentsNumber.keys())]
AllStudentsNumber_keys.sort()
print(AllStudentsNumber_keys)
AllStudentsNumberDup.sort()
problem += AllStudentsNumber_keys == AllStudentsNumberDup
#
# # 解く
# problem.solve()
#
# # 結果表示
# print("group1")
# print(group1)
# # print('group1: {group1}'.format(group1=group1.value()))
# # print('group2: {group2}'.format(group2=group2.value()))
# # print('group3: {group3}'.format(group3=group3.value()))
