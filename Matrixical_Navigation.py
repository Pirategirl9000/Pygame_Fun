
#TODO Get this class set up properly in here and add docstrings

def move(direction, matrix):
    player = get_loc(matrix)
    
    if (direction == "left" and player[1] != 0):
        store = matrix[player[0]][player[1]-1]
        matrix[player[0]][player[1]-1] = 1
        matrix[player[0]][player[1]] = store
        return matrix
    elif (direction == "right" and player[1] != 5):
        store = matrix[player[0]][player[1]+1]
        matrix[player[0]][player[1]+1] = 1
        matrix[player[0]][player[1]] = store
        return matrix
    elif (direction == "up" and player[0] != 0):
        store = matrix[player[0]-1][player[1]]
        matrix[player[0]-1][player[1]] = 1
        matrix[player[0]][player[1]] = store
        return matrix
    elif (direction == "down" and player[0] != 5):
        store = matrix[player[0]+1][player[1]]
        matrix[player[0]+1][player[1]] = 1
        matrix[player[0]][player[1]] = store
        return matrix
    else:
        return matrix
    
def get_loc(matrix):
    for row in matrix:
        for item in row:
            if item == 1:
                return [matrix.index(row), row.index(item)]
    
def show_map(matrix):
    for row in matrix:
        print(row)