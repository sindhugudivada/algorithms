def previouslengths(arr):
    for i in range (len(arr)):
	if type(arr[i])is str:
	    arr[i]=len(arr[i])
	print arr[i]    
    return arr



if __name__ == '__main__':
   print(previouslengths(["vineel","sindhu",9]))  
