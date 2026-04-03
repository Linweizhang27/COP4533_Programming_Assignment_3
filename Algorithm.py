def find_max_value(val, A, B):
    M = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if (A[i-1] == B[j-1]): #remember that A and B are still zero-indexed
                 M[i][j] = max(M[i-1][j-1]+ val[A[i-1]], M[i-1][j], M[i][j-1]) #the val dictionary is also 0-indexed!!
            else:
                M[i][j] = max(M[i][j-1], M[i-1][j])

    print(M[len(A)][len(B)])
    return M[len(A)][len(B)], M

def find_subsequence(M, val, A, B):
    i = len(A)
    j = len(B)
    result = []

    while (i>0 and j>0): #remember that A,B are 0-indexed, M is 1-indexed!!
        if (A[i-1] == B[j-1] and M[i][j] == M[i-1][j-1]+val[A[i-1]]):
            result.append(A[i-1]) #result is backwards
            i -= 1
            j -= 1
        elif (A[i-1] == B[j-1] and M[i][j] == M[i-1][j]):
            i -= 1
        elif (A[i-1] == B[j-1] and M[i][j] == M[i][j-1]):
            j -= 1
        elif (A[i-1] != B[j-1] and M[i][j] == M[i-1][j]):
            i -= 1
        elif (A[i-1] != B[j-1] and M[i][j] == M[i][j-1]):
            j -= 1
    result.reverse()
    print(result)
    return result
    

def main():
    val = {}
    val['a'] = 2
    val['b'] = 4
    val['c'] = 5

    A = ['a', 'a', 'c', 'b']
    B = ['c', 'a', 'a', 'b']

    total, M = find_max_value(val, A, B)
    find_subsequence(M, val, A, B)


if __name__ == "__main__":
    main()