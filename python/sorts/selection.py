def sort(input):
    for i in range(len(input)):
        min_element = input[i]
        for j in range(i+1, len(input)):
            if input[j] < input[min_element]:
                min_element = j
        input[i], input[min_element] = input[min_element], input[i]
