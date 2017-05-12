import os

# Read data
inputFile = open('A-large-practice.in', 'r')
header = inputFile.readline()
data = []
for line in inputFile:
	splitLine = line.split(' ')
	splitLine[0] = list(map(int,list(splitLine[0].replace('-','0').replace('+','1'))))
	data.append((splitLine[0],int(splitLine[1])))

# Create output outputFile
try:
	os.remove('output.out')
except:
	pass
outputFile = open('output.out', 'a')


for testCase in range(len(data)):
	order = data[testCase][0]
	k = data[testCase][1]
	kCurrent = 0
	counter = 0
	output = 'Case #'+str(testCase+1)+': '
	try:
		for i in range(len(order)):
			if order[i] == 0:
				for j in range(k):
					order[i+j] = not order[i+j]
				counter=counter +1
			else:
				pass
		output = output + str(counter)
	except:
		output = output + 'IMPOSSIBLE'

	outputFile.write(output+'\n')