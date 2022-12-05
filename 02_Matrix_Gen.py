# -*- coding:utf-8 -*-
# 从Transaction数据到有向邻接矩阵
# Author: Shudong YANG
# 2021-12-24
import csv
import pandas as pd

def list(L1, L2):
    for i in range(0, len(L1)):
        if L1[i] not in L2:
            L2.append(L1[i])
    return L2

def list_with_repeat(L1, L2):
    for i in range(0, len(L1)):
        L2.append(L1[i])
    return L2

def read(file_name):
    data = pd.read_excel(file_name, index_col=0)
    university = []
    new1 = []
    new2 = []
    x1 = list_with_repeat(data['毕业学校'], new1)
    x2 = list_with_repeat(data['就业学校'], new2)
    university = list(data['就业学校'], university)
    university.sort()
    print("毕业学校x1:", x1)
    print("就业学校x2:", x2)
    print("university:", university)
    return x1, x2, university

def toMatrix(out_file, list, front, end):
    header = list
    #print("list:", list)
    bool_list = []

    with open('D:\\PhD\\12-做任务\\20211202-博士师承网络\\Output\\adjacency_matrix_title.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(list)

    matrix = [[0 for _ in range(len(list))] for _ in range(len(list))]
    for i in range(0, len(front)):
        x = front[i]
        y = end[i]

        x_bool = x in list
        y_bool = y in list

        bool_list.append(x_bool)
        if x_bool == True and y_bool == True:
            x_index = list.index(x)
            y_index = list.index(y)
            matrix[x_index][y_index] += 1
        else:
            pass

    with open(out_file, 'w', newline='') as ff:
        writer = csv.writer(ff)
        for j in range(0, len(list)):
            writer.writerow(matrix[j])

    print("matrix:", matrix)
    return matrix

def main(file_name):
    x1, x2, university = read(file_name)
    matrix = toMatrix('D:\\PhD\\12-做任务\\20211202-博士师承网络\\Output\\adjacency_matrix.csv', university, x1, x2)

if __name__ == '__main__':
    file_name = 'D:\\PhD\\12-做任务\\20211202-博士师承网络\\Input\\rawdata-5800.xlsx'
    main(file_name)
