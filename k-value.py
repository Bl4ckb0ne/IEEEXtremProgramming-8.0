from collections import deque

inp = raw_input()
inp = inp.split(" ")
N = int(inp[0])
M = int(inp[1])
K = int(inp[2])

inp = raw_input()
inp = inp.rstrip('\r')
inp = inp.split(' ')

numbers = deque()
numbers.extend(inp)

Kvalue = M

for i in range(0, N):
	
	pack = list()

	for j in range(0, M):
		pack.append(int(numbers[j]))

	numbers.rotate(-1)
	pack.sort()

	if 1 <= pack[K-1] and pack[K-1] <= M:
		if Kvalue > pack[K-1]:
			Kvalue = pack[K-1]

print(Kvalue)
