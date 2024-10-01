def Brackets(s):
    #pairing_match: 
    pairs = {')': '(', ']': '[', '}': '{'}
    if len(s) == 0:
        return True
    stack = []
    for i in range(len(s)):
        if s[i] in pairs.values():
            stack.append(s[i])
        elif s[i] in pairs:
            if len(stack) == 0 or stack[-1] != pairs[s[i]]:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False
    
            