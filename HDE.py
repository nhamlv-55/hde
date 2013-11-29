sum=0
def func1(n):
	global sum
	if n==0:
		return
	else:
		process_a_line()
		n-=1
		func1(n)

def process_a_line():
	n=int(raw_input(""))
	input = raw_input("").split()
	print compute(n, 0, input)

def compute(n, i, input):
	if i==n-1:
		if int(input[i])>0:
			return int(input[i])**2
		else:
			return 0
	else:
		if int(input[i])>0:
			return int(input[i])**2+compute(n,i+1,input)
		else:
			return compute(n,i+1,input)
def main():	
	n = int(raw_input(""))
	func1(n)

main()