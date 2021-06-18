# Array Sorting, PROBLEM STATEMENT
# import timeit
def minimumSwaps(arr):
    swaps = 0
    temp = {}
    for i, val in enumerate(arr):
        temp[val] = i
    for i in range(len(arr)):
        # because they are consecutives, I can see if the number is where it belongs
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]     # Variable holder
            arr[i] = i+1
            arr[temp[i+1]] = t
            # Switch also the tmp array, no need to change i+1 as it's already good now
            temp[t] = temp[i+1]
    print(swaps)
    return(swaps)

#
# elapsed_time = timeit.timeit(minimumSwaps([4, 3, 1, 2]), number=100)/100
# print(elapsed_time)
