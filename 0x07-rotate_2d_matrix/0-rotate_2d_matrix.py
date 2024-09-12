#!/usr/bin/python3
"""
rotating a 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    this function rotates a 2D matric
    """
    length = len(matrix)

    for j in range(int(length/2)):
        y = (n - j - 1)
        for i in range(j, y):
            x = (n - 1 - i)
            temp = matrix[j][i]
            matrix[j][i] = matrix[y][j]
            matrix[x][j] = matrix[y][x]
            matrix[y][x] = matrix[i][y]
            matrix[i][y] = temp
