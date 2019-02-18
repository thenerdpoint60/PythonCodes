#TheNerdpoint60's code

names=[]
letter=[]

n=int(input("Number for names:"))#number of names
i=0
while(i<n):#storing names
    a=str(input("Enter name:"))
    names.append(a)
    i+=1
    list1=list(a)#finding the first character
    a=list1[0]
    letter.append(a)
#print(letter) can be used to print the first character
l = 0
u = n - 1
def partition(letter,l,u):
    i = l+1
    j = u
    point = letter[l]
    p=names[l]
    while(i<=j):
        while(letter[i]<point and i<u):
            i = i+1
        while(letter[j]>point):
            j = j-1
        if(i<j):#moving the names
            letter[i],letter[j] = letter[j],letter[i]
            names[i],names[j]=names[j],names[i]#swapping
            i=i+1
            j=j-1
        else:
            i+=1
    letter[l] = letter[j]
    letter[j] = point
    names[l]=names[j]#swapping
    names[j]=p
    return j
 
def quicksort(letter,l,u):
    if(l>=u):
        return
    point_loc = partition(letter,l,u)
    quicksort(letter,l,point_loc-1)#recursive call
    quicksort(letter,point_loc+1,u)#recursive call
quicksort(letter,l,u)#function call
print("After QuickSort:")
for i in names:#printing the names
    print(i)
   
    
