
# Assessment 3.7: Sorting Algorithms
# Full Name: EMELITO SUERTE
# Method: Bubble Sort

unsorted_array = ["E", "M", "L", "I", "T", "O", "S", "U", "R"]

sorted_array = unsorted_array.copy()

n = len(sorted_array)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if sorted_array[j] > sorted_array[j + 1]:
            sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]

print("Full Name: EMELITO SUERTE")
print("Unsorted Array:", unsorted_array)
print("Sorted Array:", sorted_array)
