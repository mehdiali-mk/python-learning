def armstrongNumber(n):
	numStr = str(n)
	numLen = len(numStr)
	sumOfPower = sum(int(digit) ** numLen for digit in numStr)
	return n == sumOfPower

number = int(input("Enter the number = "))
if (armstrongNumber(number)):
	print(f"\n{number} is an Armstrong number.")
else:
	print(f"\n{number} is not an Armstrong number.")