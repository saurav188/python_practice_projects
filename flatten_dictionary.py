def flatten_dictionary(d):
    if type(d)==int:
        return d
    output={}
    for key1 in d:
        if type(d[key1])==int:
            output[key1]=d[key1]
            continue
        temp=flatten_dictionary(d[key1])
        for key2 in temp:
            output[key1+'.'+key2]=flatten_dictionary(temp[key2])
    return output
d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    }
}
print(flatten_dictionary(d))
# {'a': 1, 'b.c': 2, 'b.d.e': 3}