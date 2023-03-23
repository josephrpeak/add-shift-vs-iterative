# Joe Peak
# CS5803
# 3/22/2023

def add(A, B):

	result = bin(int(A,2) + int(B,2))[2::]

	if(len(result) > len(max(A,B))):
		carry = result[0]
		result = result[1::]
	else:
		carry = '0'

	return (result.zfill(len(max(A,B))), carry)

def shift(A, Q, carry):

	length = len(A + Q)

	AQ = int(A+Q, 2)
	AQ = bin(AQ >> 1)[2::]
	AQ = str(AQ).zfill(length)

	if(carry == '1'):
		AQ = list(AQ)
		AQ[0] = '1'

	AQ = "".join(AQ)

	return AQ

def main(x,y):

	f = open("results_addshift.txt", 'a')

	# Store the number of iterations that each multiplication should run for
	n = len(max(x,y))

	# Initialize the accumulator with 0s
	A = "0"*len(max(x,y))

	# Simulate the filling of registers
	B = x 
	Q = y
	AQ = A + Q

	# Initialize carry to 0
	carry = '0'

	print()
	print(f"Performing: {x} * {y}")

	# Loop until the iteration counter hits 0
	while(n > 0):
		# Check last bit of AQ
		if(AQ[-1] == '0'):
			AQ = shift(A,Q,carry)
			carry = '0'
		elif(AQ[-1] == '1'):
			result_and_carry = add(A,B)

			# Assign A to the result portion of result_and_carry
			A = result_and_carry[0]

			# Assign carry to the carry portion of result_and_carry
			carry = result_and_carry[1]
			AQ = shift(A,Q,carry)

			# Reset carry to 0
			carry = '0'

		# Resegment A and Q from AQ so they can be used in the next iteration
		A = AQ[0:len(AQ)//2]
		Q = AQ[(len(AQ)//2)::]

		# Decrement counter
		n-=1

	# Print result
	f.write(f"{x}*{y} = {AQ} (Binary) {hex(int(AQ,2))} (Hexadecimal)\n")
	print(f"\nBinary Result: {AQ} \nHex Result: {hex(int(AQ,2))}")
	print('-----------------------------------------------------')
	f.close()
	
if __name__=="__main__":
	main(x,y)