def find_max_subsequence(val, A, B):

    M = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

    '''for i in range(len(A)+1):
        M[i][0] = 0
    
    for j in range(len(B)+1):
        M[0][j] = 0'''

    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if (A[i-1] == B[j-1]): #remember that A and B are still zero-indexed
                 M[i][j] = max(M[i-1][j-1]+ val[A[i-1]], M[i-1][j], M[i][j-1]) #the val dictionary is also 0-indexed!!
            else:
                M[i][j] = max(M[i][j-1], M[i-1][j])

    print(M[len(A)][len(B)])
    return M[len(A)][len(B)]

def main():
    val = {}
    val['a'] = 2
    val['b'] = 4
    val['c'] = 5

    A = ['a', 'a', 'c', 'b']
    B = ['c', 'a', 'a', 'b']

    find_max_subsequence(val, A, B)


if __name__ == "__main__":
    main()