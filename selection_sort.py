# Function to perform Selection Sort
def selectionSort(arr, order='asc'):
    n = len(arr)  # Get the length of the array
    for i in range(n):
        selected_idx = i  # Assume the current element is the minimum (asc) or maximum (desc)
        
        # Iterate through the unsorted part of the array
        for j in range(i + 1, n):
            # Check if we need to update selected index based on sorting order
            if (order == 'asc' and arr[j] < arr[selected_idx]) or \
               (order == 'desc' and arr[j] > arr[selected_idx]):
                selected_idx = j  # Update index of smaller/larger element

        # Swap if a new minimum/maximum is found
        if selected_idx != i:
            print(f"Swapping {arr[i]} and {arr[selected_idx]}\n")  # Show what is being swapped
            arr[i], arr[selected_idx] = arr[selected_idx], arr[i]  # Perform the swap
            print("Current array:", arr, "\n")  # Show array after swap

    return arr  # Return the sorted array

# ----- Main Program -----

# Take user input, split by spaces, convert each to integer, and store in a list
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Unsorted array:", arr, "\n")  # Show the array before sorting

# Ask user for sorting order (asc or desc)
order = input("Enter sorting order (asc/desc): ").strip().lower()
# Repeat until a valid order is entered
while order not in ['asc', 'desc']:
    order = input("Invalid input. Please enter 'asc' or 'desc': ").strip().lower()

# Call the sorting function with chosen order
selectionSort(arr, order)

# Print the sorted array
print(f"Sorted array ({order}ending):", arr)


# Greedy Algorithm: It chooses the local optimum at each step with the hope of finding the global optimum.
# Selection Sort is a classic example of a greedy algorithm because it iteratively selects the minimum element and places it in the sorted array.
#time: 	O(n²)
#space: O(1) → Constant space
#Selection Sort is used:
#When memory is very limited, For educational purposes to understand sorting, On small datasets where performance is not critical.
#bubble sort Time Complexity:Best: O(n) Average: O(n²)Worst: O(n²)#Space Complexity:O(1) (in-place sorting)
#insertion sort saem as bubble ,
#quick sort Best/Average: O(n log n) Worst: O(n²) (when pivot is poorly chosen, like sorted input) ✅ Space Complexity: O(log n) due to recursion stack , 
#merge sort(Divide-and-conquer, partitioning) ✅ Time Complexity:
#Best, Worst, Average: O(n log n)
#✅ Space Complexity:O(n) (needs extra space for merging)
