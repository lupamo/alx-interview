def pascal_triangle(n):
    """
    n is the number of rows in Pascal's Triangle generated
    returns a list of list in pascal's triangle
    """
    if n <= 0:
        return []

    tri = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = tri[i - 1][j - 1] + tri[i - 1][j]
        tri.append(row)
    return tri
