def greatest(arr):
    value=arr[1]
    count=0
    for i in range(len(arr)):
	if(value<arr[i]):
	    print arr[i]
	    count=count+1
    return count	    

if __name__ == '__main__':
   print(greatest([1,3,5,7,9,13]))  
