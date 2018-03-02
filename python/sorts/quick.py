def sort(input):
    recursive_sort(input, 0, len(input) - 1)

def recursive_sort(input, low, high):
    if low >= high:
        return
    elif low == high - 1:
        if input[low] > input[high]:
            input[low], input[high] = input[high], input[low]
        return

    pivot = partition(input, low, high)
    recursive_sort(input, low, pivot)
    recursive_sort(input, pivot + 1, high)

def partition(input, low, high):
    pivot_index = low + ((high - low + 1) / 2)
    input[low], input[pivot_index] = input[pivot_index], input[low]

    i, j = low + 1, high
    while i < j:
        if input[i] <= input[low]:
            i += 1
        else:
            input[i], input[j] = input[j], input[i]
            j -= 1
    
    if input[i] > input[low]:
        i -= 1
    input[low], input[i] = input[i], input[low]

    return i
