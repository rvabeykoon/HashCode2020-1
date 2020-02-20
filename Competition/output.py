# of libraries
library_number = 2

print(library_number)

# 2D array of library sendoffs
# First element of each array is Library #
# Second element of each array is # of books being sent
# All other elements are the book #'s being sent
library_arrays = [[1, 3, 5, 2, 3], [0, 5, 0, 1, 2, 3, 4]]

for i in range(library_number):
    print(library_arrays[i][0], end=' ')
    print(str(library_arrays[i][1]))
    for j in range(2, len(library_arrays[i])):
        print(library_arrays[i][j], end=' ')
    print()
