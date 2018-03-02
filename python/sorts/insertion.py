def sort(input):
    for i in range(1, len(input)):
        while i > 0 and input[i] < input[i-1]:
            input[i-1], input[i] = input[i], input[i-1]
            i -= 1
            
        
