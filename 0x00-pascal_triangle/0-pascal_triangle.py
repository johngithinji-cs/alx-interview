#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Create a function def pascal_triangle(n):
    that returns a list of lists of integers representing the Pascal’s triangle of n:
    '''
    list1 = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        temp_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            elif i > 0 and j > 0:
                temp_list.append(list1[i - 1][j - 1] + list1[i - 1][j])
        list1.append(temp_list)
    return list1
