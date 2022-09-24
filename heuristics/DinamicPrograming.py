def dinamic_programing(capacity,wt,val,n):
    
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n+1):
        for j in range(capacity+1):
            if i == 0 or j == 0:continue
            elif wt[i-1] <= j:
                K[i][j] = max(K[i-1][j], val[i-1]+K[i-1][j-wt[i-1]])
            else:
                K[i][j] = K[i-1][j]

    return K[n][capacity]