#ThnerdPoint60's code
#Selection Sort of Numbers
def Selection_Sort(my_list):#function call 
    for last_element in range(len(my_list)-1,0,-1):#taking the last ement till the start
        maximum_element_pos=0 
        for current_element in range(1,last_element+1):#starting the first element till the last
            if(my_list[maximum_element_pos]<my_list[current_element]):#finding the maximum element position
                maximum_element_pos=current_element
        #Swapping the elements for maximum 
        a=my_list[last_element]
        my_list[last_element]=my_list[maximum_element_pos]
        my_list[maximum_element_pos]=a
    """
        We can also swap by
        my_list[last_element],my_list[maximum_element_pos]=my_list[maximum_elemet_pos],my_list[last_element]
    """
my_list=[]
b=int(input("Enter Number of Elements in Your list:"))
c=1
while(c<=b):#for entering number in a list
    value=int(input("Enter the "+str(c)+" value:"))
    my_list.append(value)
    c+=1
Selection_Sort(my_list)#calling function
print(my_list)#printing the whole list after sort
    
