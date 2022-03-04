def cap(data,v):
	for i in range(len(data)):
		for j in range(len(data[i])):
			if data[i][j]>v:
				data[i][j]=v

def overlap(set1,list1):
	i=0
	while i<len(list1):
		if list1[i] in set1:
			i+=1
		else:
			list1.pop(i)
	set1.clear()
	for i in range(len(list1)): 
		set1.add(list1[i])
	return set1
	
def split(words):
	result={}
	for i in words:
		result[len(i)]={}
	for i in words:
		if result[len(i)]=={}:
			result[len(i)]={i}
		else:
			result[len(i)].add(i) 
	return result
	
def odds_to_back(list):
	l=len(list)
	i=0
	while i<l:
		if list[i]%2:
			list.insert(len(list),list[i])
			list.remove(list[i])
			l-=1
		else:
			i+=1
	return list

