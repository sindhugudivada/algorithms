def from_end(arr):
    value=[]
    for i in range(len(arr)):
	if i%2==1:
	    value.append(arr[-i]) 
    list=map(str,value)
    return ''.join(list)


if __name__=='__main__':
    print(from_end([9,28,3,7,9,0]))
