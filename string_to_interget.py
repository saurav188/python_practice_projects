def convert_to_int(s):
    if s[0]=='-':
        sign=-1
        s=s[1:]
    else:
        sign=1
    num_of_digit=len(s)
    result=0
    for each in s:
        result+=(ord(each)-48)*(10**(num_of_digit-1))
        num_of_digit-=1
    return result*sign
print(convert_to_int('135') + 1)
# ascii of 0==48