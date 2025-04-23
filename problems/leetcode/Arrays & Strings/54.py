def spiralOrder(matrix):
    m = len(matrix)
    n = len(matrix[0])
    answer = [0] * (m*n)

    lb = 0
    rb = 0

    print(len(answer))

print(spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
