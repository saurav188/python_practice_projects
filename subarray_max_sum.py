def max_subarray_sum(arr):
    max_value_yet=0
    max_growing_value=0
    for item in arr:
        max_growing_value+=item
        if max_growing_value>max_value_yet:
            max_value_yet=max_growing_value
        if max_growing_value<0:
            max_growing_value=0
    return max_value_yet


print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137