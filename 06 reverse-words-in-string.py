import re

def reverseWords(s):
    matches = re.findall(r'\b(\w*)\b ?', s)

    matches = [x for x in matches if x]
    reversed = matches.copy()
    reversed.reverse()

    # print(reversed)
    return " ".join(reversed)

# ============================
# tests
# ============================

print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))
print(reverseWords("a good   example"))