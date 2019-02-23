#Thenerdpoint60
#Inverse of a 2X2 Matrix
m=int(input("Enter number of rows for matrix:"))
n=int(input("Enter number of columns for matrix:"))
matrix=[] #MATRIX 1
for i in range(0,n):
    matrix.append([])
for i in range(0,m): #creating empty matrix
    for j in range(0,n):
        matrix[i].append(j)
        matrix[i][j]=0
for i in range(0,m):
    for j in range(0,n):
        print("Enter value in row: ",i+1," & column: ",j+1)
        matrix[i][j]=int(input())#input for the matrix
z=matrix[1][1]*matrix[0][0]
y=matrix[0][1]*matrix[1][0]
q=z-y#finding the determinant
if(q==0):
    print("Determinant is Zero")
else: #if not 0 and has a value
    w=1/q#1/determinant
    result=[]
    x=m
    y=n
    for i in range(0,y):
        result.append([])
    for i in range(0,x):
        for j in range(0,y):
            result[i].append(j)
            result[i][j]=0
    a=matrix[0][0]
    b=matrix[0][1]
    c=matrix[1][0]
    d=matrix[1][1]
    #(1/determinant)*(d -b
    #                -c d)
    result[0][0]=w*d
    result[0][1]=w*(-b)
    result[1][0]=w*(-c)
    result[1][1]=w*a
    for i in result:
        print(i)
    
