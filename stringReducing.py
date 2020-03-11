"""
4.	Encoding a string the below format to reduce the size of the string.A string of lowercase characters in range ascii[‘a’..’z’].
    We want to reduce the string to its shortest length by doing a series of operations. In each operation we select a pair of adjacent lowercase letters
    that match, and delete them. For instance, the string aab could be shortened to b in one operation. Now we have to delete as many characters as possible
    using this method and print the resulting string. If the final string is empty, print Empty String Function Description
"""

# aaabccddd ----→ abccddd  --------→ abddd ------→ abd

def superReducedString (s):
    input_list = list(s)
    while input_list:
        out_string = MaxReducedString(input_list)
        if out_string == input_list:
            final_string = ''.join(input_list)
            return final_string
        else:
            input_list = out_string
    return 'Empty String'

def MaxReducedString(l):
    if len(l) == 1:
        return l
    new_list=''
    i = 0
    while i < len(l):
        if i == len(l) - 1:
            new_list+=l[i]
            i += 1
        elif l[i] == l[i+1]:
            i += 2
        elif l[i] != l[i+1]:
            new_list+=l[i]
            i += 1
    return new_list

sample_data="aa"
out_data=superReducedString (sample_data)
print(out_data)