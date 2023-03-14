def find_max(Values):
    max_value = [0]
    for x in Values:
        if x > max_value:
            max_value = x
    return max_value
print()