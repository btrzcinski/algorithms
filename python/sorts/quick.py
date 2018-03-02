def sort(input):
    if len(input) <= 1:
        return input
    elif len(input) == 2:
        if input[0] > input[1]:
            return [input[1], input[0]]
        else:
            return input

    pivot = partition(input)
    left, right = input[:pivot+1], input[pivot+1:]

    return sort(left) + sort(right)

def partition(input):
    pivot_index = len(input)/2
    input[0], input[pivot_index] = input[pivot_index], input[0]

    i, j = 1, len(input) - 1
    while i < j:
        if input[i] <= input[0]:
            i += 1
        else:
            input[i], input[j] = input[j], input[i]
            j -= 1
    
    if input[i] > input[0]:
        i -= 1
    input[0], input[i] = input[i], input[0]

    return i
