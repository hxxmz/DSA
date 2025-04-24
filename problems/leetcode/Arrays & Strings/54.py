def spiralOrder(matrix):
    m = len(matrix)
    n = len(matrix[0])
    answer = [0] * (m * n)

    lb = 0
    rb = 0

    direction = 1
    horizontal = True

    # to handle bounds further maybe place an index on answer array to know how many elements scanned 
    # and cut off main loop through that, because middle indices require more than one appearances
    # think of something to handle bounds
    # you can also use directions template to escape many conditions;
    # use dirs (r,c) = ( (0,1),(1,0),(0,-1),(-1,0) ) , 0 for constant / non-zero for progression

    # to be continued
   

    print(len(answer))

print(spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
