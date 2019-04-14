#BHAVY CODE
m=int(input("Enter number of rows for matrix1:"))
n=int(input("Enter number of columns for matrix1:"))
matrix1=[] #MATRIX 1
for i in range(0,n):
    matrix1.append([])
   # matrix_2.append([])
for i in range(0,m):
    for j in range(0,n):
        matrix1[i].append(j)
        matrix1[i][j]=0
       # matrix_2[i].append(j)
       # matrix_2[i][j]=0
for i in range(0,m):
    for j in range(0,n):
        print("Enter value in row: ",i+1," & column: ",j+1)
        matrix1[i][j]=int(input())
       # matrix_2=2*matrix1[i][j]
        
m=int(input("Enter number of rows for matrix2:"))
n=int(input("Enter number of columns for matrix2:"))
matrix2=[] #MATRIX 2
for i in range(0,n):
    matrix2.append([])
for i in range(0,m):
    for j in range(0,n):
        matrix2[i].append(j)
        matrix2[i][j]=0
for i in range(0,m):
    for j in range(0,n):
        print("Enter value in row: ",i+1," & column: ",j+1)
        matrix2[i][j]=int(input())
#For addition
result1=[]
a=m
b=n
for i in range(0,b):
    result1.append([])
for i in range(0,a):
    for j in range(0,b):
        result1[i].append(j)
        result1[i][j]=0
for i in range(len(matrix1)):
     for j in range(len(matrix1[0])):
         for k in range(len(matrix2)):
              result1[i][j] += matrix1[i][k] + matrix2[k][j]

print("After Addition:",result1)


#for multiplication
result=[]
x=m
y=n
for i in range(0,y):
    result.append([])
for i in range(0,x):
    for j in range(0,y):
        result[i].append(j)
        result[i][j]=0
for i in range(len(matrix1)):
     for j in range(len(matrix2[0])):
         for k in range(len(matrix2)):
              result[i][j] += matrix1[i][k] * matrix2[k][j]
         

print("After Multiplication:",result)


#For addition 2A+B
result2=[]
a=m
b=n
for i in range(0,b):
    result2.append([])
for i in range(0,a):
    for j in range(0,b):
        result2[i].append(j)
        result2[i][j]=0
for i in range(len(matrix1)):
     for j in range(len(matrix1[0])):
         for k in range(len(matrix2)):
              result2[i][j] += (2*matrix1[i][k]) + matrix2[k][j]

print("After Addition(2A+B):",result2)

#BHAVY CODE





















