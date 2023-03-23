# Joe Peak
# CS5803
# 3/22/2023

import addshift
import iterative
import time
import random
from matplotlib import pyplot as plt

# Lists to store timings of each algorithm
results_addshift = []
results_iterative = []

# Number of times to run each multiplication (in order to generate more accurate timings)
accuracy = int(input("Enter accuracy: "))

# Values to be multiplied
multipliers = ['1110', '0101', '111111', '101110', '111011', '00011111', '11010111', '01010101', 
				'01110111', '01111000', '0101010101', '1100111011', '1001101110', '010101010101', 
				'001111100111', '101010101010', '111001110000', '1111111111110000', '1110011100010100', 
				'0100111101101110', '1100110011001100']
multiplicands = ['1111', '0101', '111111', '110111', '100011', '01010101', '01010101', '11010111', '00110011', 
				'01110111', '0101010101', '1001110000', '0101111010', '010101010101', '000011111111', '101010101010', 
				'000011111111', '0101010101010101', '1001001001001111', '1111110011001110', '1010101010101010']

# Begin add-and-shift algorithm
for i in range(len(multipliers)):

	# Keep track of total amount of elapsed time (for all iterations)
	total = 0

	for j in range(accuracy):
		start = time.time()

		# Perform the add-and-shift multiplication
		addshift.main(multipliers[i],multiplicands[i])

		end = time.time()

		# Calculate elapsed time of the algorithm
		elapsed = end - start

		# Add to total running time
		total += elapsed

	# Append the average running time for all iterations
	results_addshift.append(total/accuracy)


# Begin iterative method
for i in range(len(multipliers)):

	# Keep track of total amount of elapsed time
	total = 0

	for j in range(accuracy):
		start = time.time()

		# Perform the iterative method
		iterative.main(multipliers[i], multiplicands[i])

		end = time.time()

		# Calculate elapsed time of the algorithm
		elapsed = end - start

		# Add to total running time
		total += elapsed

	# Append the average running time for all iterations
	results_iterative.append(total/accuracy)

# Plot data
x_data1 = [len(i) for i in multiplicands]
y_data1 = results_addshift

x_data2 = [len(i) for i in multiplicands]
y_data2 = results_iterative

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(x_data1, y_data1, label = 'add-and-shift')
ax1.plot(x_data2, y_data2, label = 'iterative')
ax1.set_xlabel('# of Bits')
ax1.set_ylabel('Avg. Elapsed Time (s)')
ax1.set_title(f'Avg. Elapsed Time vs # of Bits ({accuracy} Samples)')

fig.tight_layout()

plt.show()