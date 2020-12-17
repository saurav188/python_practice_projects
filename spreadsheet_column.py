import math
def column_name(n):
    if n<=26:
        return str(chr(64+n))
    m=math.floor(n/26)
    n=n-(26*m)
    return str(chr(64+m))+str(column_name(n))

print(column_name(26))
print(column_name(27))
print(column_name(28))
print(column_name(53))
# Z
# AA
# AB