#A UTF-8 character encoding is a variable width 
#character encoding that can vary from 1 to 4 bytes 
#depending on the character. 
#The structure of the encoding is as follows:
#1 byte:  0xxxxxxx
#2 bytes: 110xxxxx 10xxxxxx
#3 bytes: 1110xxxx 10xxxxxx 10xxxxxx
#4 bytes: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
#For more information, you can read up on the Wikipedia Page.

#Given a list of integers where each integer represents 1 byte, 
#Return whether or not the list of integers is a valid UTF-8 encoding.

BYTE_MASKS = [
    None,
    0b10000000,
    0b11100000,
    0b11110000,
    0b11111000,
]
BYTE_EQUAL = [
    None,
    0b00000000,
    0b11000000,
    0b11100000,
    0b11110000,
]

def utf8_validator(bytes):
    no_bytes=len(bytes)
    if no_bytes==0 or no_bytes>4:
        return False
    elif no_bytes==1:
        if bytes[0]!=0:
            return False
    else:
        temp=0
        for i in range(no_bytes):
            temp+=(2**(7-i))
        if temp!=bytes[0]:
            return False
        for i in range(1,no_bytes):
            if bytes[i]!=(10**7):
                return False
    return True

print(utf8_validator([0b00000000]))
# True
print(utf8_validator([0b00000000, 10000000]))
# False
print(utf8_validator([0b11000000, 10000000]))
# True