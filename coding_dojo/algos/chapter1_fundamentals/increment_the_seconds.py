def increment(arr):
    for i in range (len(arr)):
	if arr[i]%2==1:
	    arr[i]=arr[i]+1
	print arr[i]    
    return arr



if __name__ == '__main__':
   print(increment([2,4,5,9]))  
