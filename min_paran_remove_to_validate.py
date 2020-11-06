def count_invalid_parenthesis(string):
    count=0
    open_paran=0
    for each in string:
        if open_paran==0 and each==')':
            count+=1
        elif each=='(':
            open_paran+=1
        elif each==')':
            open_paran-=1 
    return count+open_paran
print(count_invalid_parenthesis("()())()))()()("))