def palindromeIndex(s):
    result1 = -1
    
    for i in range(len(s)):
        fl, ll = i, len(s) - i - 1
        if fl <= ll and ll >= fl:
            if s[fl] == s[ll]:
                result1 += 0
            else:
                result1 = 0
                
    if result1 == -1:
        return result1
    
    for i in range(len(s)):
        fl, ll = i, len(s) - i - 1
        
        if fl <= ll and ll >= fl:
            if s[fl] != s[ll]:
                fl += 1
                if s[fl] != s[ll]:
                    ll -= 1
                    fl -= 1
                else:
                    return fl - 1
                if s[fl] != s[ll]:
                    return -1
                else:
                    return ll + 1