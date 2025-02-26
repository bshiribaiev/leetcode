'''
    My thoughts:
    Need to return the strings that do not appear in the first one
    and it is case sensitive
    
    Need to make sure that they are returned in order that they appear 
    in s

def missingWords(s, t):
    
    # create a list of strings that will be returned
    result = []
    
    # make list from t and index to make it easier to iterate
    t_list = t.split()
    idx = 0
    
    # iterate through words in a list string and check if they are not in t 
    for word in s.split():
        
        # make sure to follow the order of words
        if (idx < len(t_list)):
            if word == t_list[idx]:
                idx += 1
            
            else:
                result.append(word)
                
        # append the rest of the words    
        else:
            result.append(word)
    
    # return the resulting list with missing words
    return result'''
new_l = []
logs = ["9 7 50", "22 7 39"]
for i in logs:
     new_l.append(" ".join(i.split()[:2]))
            
print (new_l)