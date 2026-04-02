def find_max_subsequence(val, A, B):
    M = []
    
    for i in range(len(A)):
        M[i][0] = 0
    
    for j in range(len(B)):
        M[0][j] = 0

    for i in range(len(A)):
        for j in range(len(B)):
            if (A[i] == B[j]):
                 M[i][j] = max(M[i-1][j-1]+ val[A[i]], M[i-1][j], M[i][j-1])
            else:
                M[i][j] = max

                 