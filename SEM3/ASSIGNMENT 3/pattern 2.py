def generate_spiral(n):
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n-1, 0, n-1
    num = 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1        
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1    
    return matrix

def print_spiral(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
N = int(input("Enter the number of lines N: "))
spiral_matrix = generate_spiral(N)
print_spiral(spiral_matrix)

