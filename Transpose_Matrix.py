#thenerdpoint60's code
#Finding the transpose of the matrix of the same rows and column
m=int(input("Enter number of rows for matrix1:"))
n=int(input("Enter number of columns for matrix1:"))
matrix1=[] #MATRIX 1
matrix2=[] #Matrix 2 the transpose matrix
for i in range(0,n):
    matrix1.append([])
    matrix2.append([])
for i in range(0,m): #creating empty matrix
    for j in range(0,n):
        matrix1[i].append(j)
        matrix1[i][j]=0
        matrix2[i].append(j)
        matrix2[i][j]=0

        
for i in range(0,m):
    for j in range(0,n):
        print("Enter value in row: ",i+1," & column: ",j+1)
        matrix1[i][j]=int(input())#input for the matrix

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        matrix2[j][i]=matrix1[i][j]#transposing the matrix

for i in matrix2:
    print(i)#printing the transpose matrix
