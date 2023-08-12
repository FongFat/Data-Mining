def find_LCS(X, Y):
    # Create a lcss matrix
    lcss = [[0] * (len(Y) + 1) for i in range(len(X) + 1)]

    # Build the matrix following the algorithm
    for i in range(len(X) + 1):
        for j in range(len(Y) + 1):
            if i == 0 or j == 0 :
                lcss[i][j] = 0
            elif X[i - 1] == Y[j - 1] :
               lcss[i][j] = lcss[i-1][j-1] + 1
            else :
                lcss[i][j] = max(lcss[i-1][j], lcss[i][j-1])


    # Initialization for backtracking
    i = len(X)
    j = len(Y)
    index =  lcss[i][j]
    LCS = [""] * (index + 1)
    LCS[index] = ""


    # Backtrack
    while i > 0 and j > 0 :
        if X[i-1] == Y[j-1]:
            LCS[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        else :
            if lcss[i][j-1] > lcss[i-1][j] :
                j -= 1
            else :
                i -= 1

    print("Longest Common Subsequence Length : ", lcss[len(X)][len(Y)])
    print("LCSS: " + "".join(LCS))



if __name__ == "__main__":

    # Get the source and target string
    print("Enter the string X :")
    X = input().strip()
    print("Enter the string Y :")
    Y = input().strip()
    print("X : ", X)
    print("Y : ", Y)
    find_LCS(X, Y)

         

    
