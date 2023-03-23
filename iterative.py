# Joe Peak
# CS5803
# 3/22/2023

def main(x,y):

	f = open("results_iterative.txt", 'a')

	print()
	print(f"Performing: {x} * {y}")

	# Split each value into upper and lower halves
	a = x[0:(len(x)//2)]
	b = x[(len(x)//2)::]
	c = y[0:(len(y)//2)]
	d = y[(len(y)//2)::]

	# Get the length of the values (should be equal)
	n = len(x)

	# Convert each half to an integer in order to be multiplied
	a = int(a, 2)
	b = int(b, 2)
	c = int(c, 2)
	d = int(d, 2)

	# Perform the multplication
	res = (2**n)*(a*c)+2**(n/2)*(a*d+b*c)+b*d

	# Convert back to binary, strip the '0b'
	res = str(bin(int(res)))[2::]

	# Print result
	f.write(f"{x}*{y} = {res.zfill(2*n)} (Binary) {hex(int(res,2))} (Hexadecimal)\n")
	print(f"\nBinary Result: {res} \nHex Result: {hex(int(res,2))}")
	print('-----------------------------------------------------')
	f.close()

if __name__ == "__main__":
	main(x,y)