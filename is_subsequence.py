def isSubsequence(s, t):
# mine that only partially works and is overly complicated
# (also the problem SAID use two pointers and i'm not doing that—why?)
    indexes = []
    if s in t:
        return True
    if len(s) == len(t) and s != t:
        return False
    for i in range(len(s)):
        if s[i] not in t:
            return False
        else:
            indexes.append(t.find(s[i]))
            
    in_order = indexes.copy()
    in_order.sort()
    return in_order == indexes

# someone else's (possible) answer that uses 2 pointers and solves it easily
              
    # i = 0
    # j = 0
    # while i < len(s) and j < len(t):
    #     if s[i] == t[j]:
    #         i += 1
    #     j += 1
    # return i == len(s)        

# ============================
# tests
# ============================
print(isSubsequence('abc', 'ahbgdc'))           # True
print(isSubsequence('acb', 'ahbgdc'))           # False
print(isSubsequence('axc', 'ahbgdc'))           # False
print(isSubsequence('ab', 'baab'))              # True
print(isSubsequence('aaaaaa', 'bbaaaa'))        # False
print(isSubsequence('bb', 'ahbgdc'))            # False 