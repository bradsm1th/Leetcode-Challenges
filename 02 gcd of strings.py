# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

# ============================
# V1 (this partially works...leaving comments)
# ============================
# def gcdOfStrings(str1: str, str2: str) -> str:
#     result = ''
    
#     # easy: none of str2 matches
#     if len(str2) < len(str1) and str2 not in str1:
#         print("no match ", end='')
#         return result
#     # easy: all of str2 matches
#     elif len(str1) % len(str2) == 0 and str2 in str1:
#         print("testing full match…")
#         if str2 * int((len(str1) / len(str2))) == str1:
#             result = str2
#         return result
    
#     # less easy: part of str2 matches
#     # i'm only here if there's a match that's not exact
#     else:
#         count = len(str2) - 1 
#         while count:
#             next_str_to_try = str2[0:count]
#             divides_evenly = len(str1) % len(next_str_to_try) == 0
#             how_many_times = len(str1) // len(next_str_to_try)

#             print(f"Now trying:\t {next_str_to_try}")
#             test_str = next_str_to_try * how_many_times
#             if test_str == str1:
#                 print(f"Match! \t\t {test_str}")
#                 return next_str_to_try
#             else:
#                 count -= 1 
#             print(test_str == str1)
        
    

# ============================
# V1.1 (same as V1 without comments)
# ============================
# def gcdOfStrings(str1: str, str2: str) -> str:
#     result = ''
    
#     # easy: none of str2 matches
#     if str2 not in str1:
#         return result
#     # easy: all of str2 matches
#     elif len(str1) % len(str2) == 0 and str2 in str1:
#         result = str2
#         return result
#     # less easy: part of str2 matches
#     else:
#         count = len(str2) - 1 
#         while count:
#             next_str_to_try = str2[0:count]
#             how_many_times = len(str1) // len(next_str_to_try)

#             test_str = next_str_to_try * how_many_times
#             if test_str == str1:
#                 return next_str_to_try
#             else:
#                 count -= 1 


# ============================
# V3
# ============================        
def gcdOfStrings(str1: str, str2: str) -> str:
    # result = ''
    # bigger = max(str1, str2)
    # smaller = min(str1, str2)

    # # loop over smaller, slicing it til it's empty
    # test_string = smaller
    # while smaller:
        
    #     big_remainder = len(bigger) % len(smaller)
    #     small_remainder = len(smaller) % len(smaller)
        
    #     if big_remainder == 0 and small_remainder == 0:
    #         if (int(len(bigger) / len(smaller)) * smaller == bigger) and (int(len(test_string) / len(smaller)) * smaller == test_string):
    #             result = smaller
    #             return result
    #         else:
    #             smaller = smaller[:len(smaller) - 1]
    #         # str1 and str2 were evenly divisible but the chars didn't match
    #     else:
    #         smaller = smaller[:len(smaller) - 1]
            
            
    # if result == '':
    #     print("These strings don't have a common divisor")
    #     return result


# ============================
# someone else's answer—amazing!
# ============================
        long_word = max(str1, str2)
        short_word = min(str1, str2)
        
        # i'm adding this: are the sums equal? if not, don't bother
        if long_word + short_word != short_word + long_word:
            return ''
        
        for i in range(len(short_word),0,-1):
            print(i)
            if long_word == short_word[:i]*int(len(long_word)/i) and short_word == short_word[:i]*int(len(short_word)/i):
                return short_word[:i]
        return ''


# ============================
# tests
# ============================
# print(gcdOfStrings('ABCABC', 'ABC'))        # 'ABC'
# print(gcdOfStrings('ABABAB', 'ABAB'))       # 'AB'
print(gcdOfStrings('LEET', 'CODE'))         # ''
print(gcdOfStrings('ABCDEF', 'ABC'))        # ''

# this is just 5 and 9
print(gcdOfStrings('TAUXXTAUXXTAUXXTAUXXTAUXX', 'TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX')) 