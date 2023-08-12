def manhattan_distance(x, y):
    distance = [[0] * (len(y)) for i in range(len(x))]
    for i in range(len(y)):
        for j in range(len(x)):
            distance[i][j] = abs(x[i] - y[j])
    
    return distance


def compute_dtw(x, y):
    dist = manhattan_distance(x, y)

    # Create a DTW matrix
    dtw = [[0] * (len(y)) for i in range(len(x))]

    # Initialize the required values of the matrix
    dtw[0][0] = dist[0][0]
    for i in range(len(y)):
        dtw[i][0] = dist[i][0] + dtw[i - 1][0]

    for j in range(len(x)):
        dtw[0][j] = dist[0][j] + dtw[0][j - 1]

    # Build the matrix following the algorithm
    for i in range(1, len(y)) :
        for j in range(1, len(x)) :
            dtw[i][j] = dist[i][j] + min(dtw[i][j- 1], \
                                        dtw[i - 1][j], \
                                        dtw[i - 1][j - 1])
    # Print path 
    i = len(y) - 1
    j = len(x) - 1
    path = []
    path.append(dtw[i][j])
    while i != 0 or j != 0 :
        min_dtw = min(dtw[i][j- 1], \
                        dtw[i - 1][j], \
                        dtw[i - 1][j - 1])
        
        path.append(min_dtw)

        if min_dtw == dtw[i][j- 1] :
            j -= 1
        elif min_dtw == dtw[i - 1][j] :
            i -= 1
        else :
            i -= 1
            j -= 1

    return path
        

            
if __name__ == "__main__":

    Series_1 = [1, 7, 4, 8, 2, 9, 6, 5, 2, 0]
    Series_2 = [1, 2, 8, 5, 5, 1, 9, 4, 6, 5]
    print("X : ", Series_1)
    print("Y : ", Series_2)
    print("PATH : ", compute_dtw(Series_1, Series_2))