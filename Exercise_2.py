# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1] # move the pivot to its correct position
    return i+1

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low >= high: # single element is already sorted
        return

    pivot = partition(arr,low, high) # partition and return pivot index
    quickSort(arr, low, pivot-1) # sort the left
    quickSort(arr, pivot+1, high) # and right of the pivot
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:", arr) 
  
 
