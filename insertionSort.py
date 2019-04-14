def insertionSort(a):
    for i in range (1,len(a)):
        temp =a[i]
        k=i
        while k>0 and temp < a[k-1]:
            a[k]=a[k-1]
            k-=1
        a[k]=temp
    
  
