import csv
import re
#read txt method two
f = open("./examples/out.txt")
a1 = [[-1 for i in range(21)] for j in range(2000) ] 
b1 = [[-1 for i in range(21)] for j in range(2000) ] # 初始状态
# print(a1)
for line in f:
    sp = line.split()
    # if len(sp) > 1 and len(sp[-1].split("#")) > 1:
    #     # eleid = sp[0]
    #     data = re.split(r"([#])", sp[-1])
    #     # print(sp[0], re.split(r"([#])", sp[-1]))
    #     a1[int(sp[0])][int(data[-1]) + 1] = hex(int(sp[1],2))
    #     a1[int(sp[0])][0] = data[0]
    if len(sp) > 1 and len(sp[-1].split("@")) > 1:
        # eleid = sp[0]
        data = re.split(r"([@])", sp[-1])
        # print(sp[0], re.split(r"([@])", sp[-1]))
        try:
            a1[int(sp[0])][int(data[-1]) + 1] = hex(int(sp[1],2))
            a1[int(sp[0])][0] = data[0]
        except ValueError as ve:
            # print(f'You entered {sp[0]}, which is not a positive number.')
            a1[int(sp[0])][int(data[-1]) + 1] = [sp[1],sp[2]]
            a1[int(sp[0])][0] = data[0]
for i in range(len(a1)):
    if a1[i][0] != -1:
        print(a1[i])