def main():
	with open('milkvisits.in') as file:
		lines = file.read().splitlines()
		ans = []
		n = int(lines[0].split(" ")[0])
		#print(n)
		m = int(lines[0].split(" ")[1])
		types = lines[1];
		dictionary = {}
		for i in range (0,int(n)):
			dictionary[i+1] = []
		for i in range (0,int(n)-1):
			v = int(lines[2+i].split(" ")[0])
			w = int(lines[2+i].split(" ")[1])
			#print (dictionary, a, b)
			dictionary[v].append(w)
			dictionary[w].append(v)
		#print(dictionary)
		for i in range (0,int(m)):
			start = int(lines[1+i+int(n)].split(" ")[0])
			end = int(lines[1+i+int(n)].split(" ")[1])
			want = lines[1+i+n].split(" ")[2]
			if happy(dictionary, start, end, types, want):
				ans.append(1)
			else :
				ans.append(0)
			#print (str(ans))
	with open('milkvisits.out', 'w') as file:
		for item in ans:
			file.write(str(item))


	


def happy (dictionary, start, end, types, want):
	if (want == types[start-1] or want == types[end-1]): 
		#print(start, end, want, "true")
		return True
	elif (start == end and types[start-1] != want):
		return False
	at = int(start)
	path = {}
	togo = []
	been = []
	
	while True:
		#print(path)
		#print(at, been)
		if at not in been:
			for item in dictionary[int(at)]:
				if int(item) not in been:
					togo.append(item)
					path[int(item)] = int(at) 
				#print("togo", togo , "been", been, "path", path)
			been.append(at)
		at = int(togo[0])
		del togo[0]
		if(at == end):
			break
	#print(path, at)
	while True:
		#print(at, "-->", path[at])
		at  = int(path[at])
		if(at == start):
			break
		#print("at", at)
		#print(types[at-1])
		if types[int(path[at]-1)] == want :
			been.clear()
			togo.clear()
			path.clear()
			return True
	#print("yay")
	been.clear()
	togo.clear()
	path.clear()		
	return False


# def string types
# def int n 

if __name__ == '__main__':
	main()