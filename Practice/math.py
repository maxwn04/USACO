import math

def main():
	n = 0
	counter = 0
	while True:
		counter += 1
		n += counter
		if math.sqrt(n)%1 == 0 and counter >288:
			break
	print(counter)


# def order(counter,n):
	

if __name__ == '__main__':
	main()