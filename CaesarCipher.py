def caesarCipher(s, k):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_s = [] 

    for char in s:
        if char.isalpha():
            newi = alphabet.index(char.lower())
            
            if char.isupper():
                new_s.append(alphabet[(newi + k) % 26].upper())
            else:    
                new_s.append(alphabet[(newi + k) % 26])
        else:
            
            new_s.append(char) 
        
    return ''.join(new_s)
