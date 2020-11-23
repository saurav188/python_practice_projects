class Solution(object):
    def compress(self, chars):
        i=1
        char_count=1
        current_char=chars[0]
        result=[]
        for i in range(1,len(chars)):
            if current_char==chars[i]:
                char_count+=1
                continue
            result.append(current_char)
            if char_count!=1:
                result.append(char_count)
            current_char=chars[i]
            char_count=1
        result.append(current_char)
        if char_count!=1:
            result.append(char_count)
        return result
print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'c']))
#                         ['a', '2', 'b', 'c', '3']