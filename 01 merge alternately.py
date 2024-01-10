# test cases
# "abc"
# "pqr"
# "ab"
# "pqrs"
# "abcd"
# "pq"


# ============================
# V1
# ============================
# def mergeAlternately(word1: str, word2: str) -> str:
#     result = []
  
#     for letters in zip(word1, word2):
#         result.append(''.join(letters))
            
#     result.append(word1[len(word2):])
#     result.append(word2[len(word1):])

#     return ''.join(result)


# ============================
# V2
# ============================
# def mergeAlternately(word1: str, word2: str) -> str:
#     result = []
  
#     for letters in zip(word1, word2):
#         result.append(''.join(letters))
    
#     result.append(word1[len(word2):])
#     result.append(word2[len(word1):])

#     return ''.join(result)

# ============================
# V3
# ============================
def mergeAlternately(word1: str, word2: str) -> str:
    result = ''
  
    for letters in zip(word1, word2):
        result += (''.join(letters))
    
    if len(word1) > len(word2):
        result += word1[len(word2):]
    if len(word1) < len(word2):
        result += word2[len(word1):]

    return result


# ============================
# tests 
# ============================
print(mergeAlternately('ABC', 'pqr'))
print(mergeAlternately('abc', 'PQRST'))
print(mergeAlternately('ABCDEFGH', 'pqrst'))