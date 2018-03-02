def sort(input):
    if len(input) <= 1:
        return input

    left, right = input[:len(input)/2], input[len(input)/2:]
    left = sort(left)
    right = sort(right)

    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) == 0:
            result.append(right.pop(0))
        elif len(right) == 0 or left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    return result
