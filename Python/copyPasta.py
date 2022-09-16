def main():
	with open ('test.in') as file:
		lines = file.read().splitlines()
    	split = lines[0].split()
    	n = int(split[0])
		
	with open('test.out', 'w') as file:        
        file.write(str(ans))


if __name__ == '__main__':
	main()