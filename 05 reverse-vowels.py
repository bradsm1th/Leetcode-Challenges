def reverseVowels(s):
    s_as_list = list(s)
    
    vowel_indices = [index for index in range(len(s_as_list)) if s_as_list[index] in 'aeiouAEIOU']
    print(vowel_indices, "<- vowel indexes")        
    reversed_indices = vowel_indices.copy()
    reversed_indices.reverse()
    print(reversed_indices, "<- vowel indexes reverse order")
    
    mid = round(len(vowel_indices) / 2)
    
    for i in range(mid):
            # print(f"I need to swap '{s_as_list[vowel_indices[i]]}' for '{s_as_list[reversed_indices[i]]}'")
            # do the swapping
            [s_as_list[vowel_indices[i]], s_as_list[reversed_indices[i]]] = [s_as_list[reversed_indices[i]], s_as_list[vowel_indices[i]]]
    
    return ''.join(s_as_list)


# examples
print(reverseVowels('hello'))   # 'holle'
print(reverseVowels('leetcode'))   # 'leotcede'
print(reverseVowels('Naomi, did I moan?'))   # 'NaomI, did i moan?'