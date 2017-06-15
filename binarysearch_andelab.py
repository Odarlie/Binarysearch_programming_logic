def BinarySearch(the_list, item_to_search):
    '''
binary search function
'''
    start_position=0 
    last_position=len(the_list)-1 
    found=False
    while start_position<=last_position and notfound:  
        midpoint=(start_position+last)//2 
        if the_list[midpoint]==item_to_search: 
            found=True
        else:
            if item_to_search<the_list[midpoint]:
                last_position=midpoint-1
            else:
                start_position=midpoint+1 
        return found
