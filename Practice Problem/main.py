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


prefixSum = [0 for x in range(len(pizza_types) + 1)]
for i in range(len(pizza_types)):
    prefixSum[i + 1] = prefixSum[i] + pizza_types[i]


print(pizza_types)
print("M = " + str(M))
print(prefixSum)


nums = []
values = []
ans = 0
for i in range(len(prefixSum) - 1, 0, -1):
    for j in range(len(pizza_types)):
        diff = prefixSum[i] - pizza_types[j]
        if diff <= M:
            nums.append(diff)
            temp = pizza_types[:i]
            temp.remove(pizza_types[j])
            values.append(temp)
            break

    if prefixSum[i] <= M:
        nums.append(prefixSum[i])
        values.append(pizza_types[:i])
        break
        
print(nums)
print(values)

maxSumIndex = nums.index(max(nums))
orders = values[maxSumIndex]
orderIndexes = [pizza_types.index(order) for order in orders]
print(orderIndexes)

ans = ''
for num in orderIndexes:
    ans += str(num) + ' '
K = len(orderIndexes)


# Writing file
outputFile = filename[:filename.find('.')] + '_out.txt'
with open(outputFile, 'w') as file:
    file.write(str(K) + '\n')
    file.write(ans)
file.close()
