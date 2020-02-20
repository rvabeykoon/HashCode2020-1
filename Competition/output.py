# of libraries
library_number = 2

f = open('output.txt', 'w+')
f.write("%d\n" % library_number)

# 2D array of library sendoffs
# First element of each array is Library #
# Second element of each array is # of books being sent
# All other elements are the book #'s being sent
library_arrays = [[1, 3, 5, 2, 3], [0, 5, 0, 1, 2, 3, 4]]

for i in range(library_number):
    f.write("%d " % library_arrays[i][0])
    f.write("%d\n" % library_arrays[i][1])
    for j in range(2, len(library_arrays[i])):
        f.write("%d " % library_arrays[i][j])
    f.write("\n")
