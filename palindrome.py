def isPalindrome(a):   
    i=0
    j=len(a)-1
    while(i<j and a[i]==a[j]):
        i+=1
        j-=1
    if(i<j):
        print("Not a palindrome")
        return 0
    else:
        print("palindrome")
        return 1
    
