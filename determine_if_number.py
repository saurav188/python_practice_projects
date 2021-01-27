#"123" # Integer
#"12.3" # Floating point
#"-123" # Negative numbers
#"-.3" # Negative floating point
#"1.5e5" # Scientific notation

def parse_number(s):
    if len(s)==0:
        return True
    is_valid=True
    valid_characters={
        '1':True,'2':True,'3':True,
        '4':True,'5':True,'6':True,
        '7':True,'8':True,'9':True,
        '0':True
    }
    is_negative=s[0]=="-"
    if is_negative:
        is_valid=is_valid and parse_number(s[1:])
    is_decimal=False
    decimal_index=None
    is_scientific_no=False
    scientific_index=None
    for i in range(len(s)):
        if s[i]==".":
            is_decimal=True
            decimal_index=i
        elif s[i]=="e":
            is_scientific_no=True
            scientific_index=i
        else:
            is_valid=is_valid and valid_characters.get(s[i])
    if is_decimal and is_scientific_no:
        is_valid=is_valid and parse_number(s[:decimal_index]) and parse_number(s[decimal_index+1:scientific_index]) and parse_number(s[scientific_index+1:])
    elif is_decimal:
        is_valid=is_valid and parse_number(s[:decimal_index]) and parse_number(s[decimal_index+1:])
    elif is_scientific_no:
        is_valid=is_valid and parse_number(s[:scientific_index]) and parse_number(s[scientific_index+1:])
    if is_valid==None:
        return False
    return is_valid

print(parse_number("12.3"))
# True

print(parse_number("12a"))
# False