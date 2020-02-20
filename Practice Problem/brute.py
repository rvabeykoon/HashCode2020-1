from itertools import combinations

# filename = 'a_example.in'
filename = 'b_small.in'
# filename = 'c_medium.in'
# filename = 'd_quite_big.in'
# filename = 'e_also_big.in'

file = open(filename, 'r')
lineCount = 0
pizza_types = []
M = 0
N = 0

# Reading file
for line in file:
    line = list(map(int, line.split(' ')))
    if lineCount == 0:
        M = line[0] # maximum slices
        N = line[1] # number of types
    else:
        pizza_types = line
    lineCount += 1

file.close()

maxTypes = tuple()
maxSum = 0

for i in range(1, N):
    # Generate all combinations
    combs = list(combinations(pizza_types, i))
    for comb in combs:
        print(comb)
        total = sum(comb)
        # Update maxTypes list and maxSum
        if total > maxSum and total <= M:
            maxSum = total
            maxTypes = comb

K = len(maxTypes)
orders = ""
for t in maxTypes:
    orders += str(pizza_types.index(t)) + " "

# Writing file
outputFile = filename[:filename.find('.')] + '_out.txt'
with open(outputFile, 'w') as file:
    file.write(str(K) + '\n')
    file.write(orders)
file.close()
