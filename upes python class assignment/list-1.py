
# program to print sum, average, max, min and cummulative sum of the list 
def operations(lst):
    sum = 0
    list2 = []
    
    for i in range(len(lst)):
        sum = sum + lst[i] # calculating total sum of the list
        list2.append(sum) #calculating cummulative sum of the list
        
    print(list2)     
        
    print(f"sum of list elements is: {sum}") # printing the total sum
    print("average of list elements is : ", sum/len(lst)) # printing the average of sum
   
    max =  0
    min = lst[0]
    
    for i in range(len(lst)):
        if max < lst[i]: # condition to find maximum element in a list
            max = lst[i]
        elif min > lst[i]: # condition to find minimum element in a list
            min = lst[i]   
            
    print("max is: ", max)  # printing maximum      
    print("min is: ", min)  # printing minimum      
         
    # asking from user to enter the elements 
print("enter the elements of a list")

lst = []
for i in range(0,5):
    user_input = int(input())
    lst.append(user_input)
    
print(lst) # printing the list entered by user
operations(lst) # calling the method to perform operations on list

