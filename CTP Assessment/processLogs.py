'''
    My thoughts:
    Need to return a list of strings that denotes the user id of 
    suspiciours user that were involved in threshold number of log entries
    
    Ids should be ordered in ascending
    
    Applications logs and threshold are provided as parameters
    
    Make sure - even if the same id appears twice in one log, it counts as one transaction
    
    I think the amount of the transaction doesn't really matter for this problem
    
'''

def processLogs(logs, threshold):
    # result list to return
    result = []
    
    # make a new list that will store only ids to make it easier to iterate
    new_l = []
    
    # hashmap to track occurences of ids in transactions
    id_count = {}
    
    # store only ids in a new list
    for trn in logs:
        s, r, a = trn.split()
        new_l.append(f"{s} {r}")
    
    # iterate through ids and count their occurences
    for ids in new_l:
        s, r = ids.split()
        
        # store the number of times ids appear
        id_count[s] = id_count.get(s, 0) + 1
        id_count[r] = id_count.get(r, 0) + 1
    
    # check if the values are greater or equal to threshold    
    for ids, value in id_count.items():
        if value >= threshold:
            result.append(ids)   
            
    result.sort()
    return result