def first_non_repeating_character(s):
    # Write your code here
    count = {}
    que = deque()
    for i in range (len(s)):
        l = s[i]
        count[l] = count.get(l, 0) + 1
        
        if count[l] == 1:
            que.append((l, i))
            
        while que and count[que[0][0]] > 1:
            que.popleft()    

    if que:
        return que[0][1]
    else:
        return -1
