def palindromeIndex_1(s):
    # Write your code here
    if s == s[::-1]:
        return -1
    n = len(s)
    
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            if s[i+1] != s[n - i - 1]:
                if s[i] != s[n - i - 2]:
                    break
                else:
                    return (n - 1 - i)
            else:
                return i