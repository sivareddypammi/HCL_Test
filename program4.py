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