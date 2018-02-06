def max_of_array(arr):
    max=arr[0]
    for i in range (len(arr)):
	if arr[i]>max:
	    max=arr[i]
    print max

if __name__=='__main__':
    max_of_array([1,2,3,4,5])
