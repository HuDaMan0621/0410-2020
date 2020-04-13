def has_same_digit_freqency(list1, list2):
    #if the lengths are the same - making my life eaiser beacuse if the lengths is not the same, it will never be the same.
    if len(list1) != len(list2):
        return False

    #make a for loop that checks through each item in a list1
   

    #this part of code will show up in a lot of places
    # #dictionary 1{
    #     1: 2
    #     2: 1
    #     3: 1
    #     4: 1
    # #}


    dictionary1 = {} #blank dictionary 
    for num in list1:
        if dictionary1.get(num, False):
            dictionary1[num] += 1 #the number 1 is assigned to the number at this times
            # dictionary1[num] = dictionary1[num] + 1
            #dictionary [num] += 1 if there's value add 1 to it
        else:
            dictionary1[num] = 1

    #for index in range(len(list1)):
        
        
        #print(list1[index])
    #make a dictionary to count how many times something is in a list1

    #make a second dictionary to count how many times something shows up in the second list 
    dictionary2 = {}
    for num in list2:
        if dictionary2.get(num, False):
            dictionary2[num] += 1 #the number 1 is assigned to the number at this times
            # dictionary1[num] = dictionary1[num] + 1
            #dictionary [num] += 1 if there's value add 1 to it
        else:
            dictionary2[num] = 1
    # #{
    #     4: 1
    #     3: 1
    #     2: 1
    #     1: 2
    # }
    #check dictionaries to see if the counts are the same 
    '''
    #if you didn't know how to do the following
    if dictionary 1 == dictionary2:
        return True
    else:
        retrun False
    '''

    #use this method

    for key in dictionary1.keys():
        if dictionary2[key] != dictionary1[key]:
            return False
    
    return True

print ('hello')
print (has_same_digit_freqency([1,2,3,4][4,3,2,1]))