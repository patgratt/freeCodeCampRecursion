# the freecode camp was confusing as hell this solution is much  better 
arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0 # left_arr idx
        j = 0 # right_arr idx
        k = 0 # merged arr idx
        # this will iterate our pointers thru the arrays
        while i < len(left_arr) and j < len(right_arr):
            # if the left value is lower
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            # if the right value is lower
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        # if the left pointer didn't get incremented bc it was higher
        while i < len(left_arr):
            arr[k] = left_arr[i] 
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
        

arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
merge_sort(arr_test)
print(arr_test)



# notice how this doesn't work, therefore it must be the case that when the recursive calls are invoked  it still goes thru
# the whole function
def merge_sort_mini(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

arr_test2 = [4, 2, 9, 0, -1, 88, 93, 3, 2, 0]
merge_sort_mini(arr_test2)
print(arr_test2)
