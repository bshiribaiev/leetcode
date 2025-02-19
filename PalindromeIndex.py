def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    n = len(s)
    
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            if s[i+1:n-i] == s[i+1:n-i][::-1]:
                return i
            if s[i:n-1-i] == s[i:n-1-i][::-1]:
                return n-1-i
                
            break
    return -1
