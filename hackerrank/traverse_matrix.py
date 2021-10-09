# https://www.geeksforgeeks.org/traverse-a-given-matrix-using-recursion/

M=3 #Col 
N=2 #Row


# Function to traverse the matrix
def traverseMatrix(arr, current_row, current_col):
    # If the entire column is traversed
    if current_col >= M:
        return 0
    
    # If the entire row is traversed
    if current_row >= N:
        return 1

    # Print the value of the current cell of the matrix
    print(arr[current_row][current_col], end=", ")

    # Recursive call to traverse the matric in horizontal direction
    if (traverseMatrix(arr, current_row, current_col + 1 ) == 1):
        return 1
    
    # Recrusive call for changing the row of the matrix
    return traverseMatrix(arr, current_row + 1, 0)

#driver code
if __name__ == "__main__":
    arr =   [[1,2,3],
            [4,5,6]]
    traverseMatrix(arr, 0, 0)
