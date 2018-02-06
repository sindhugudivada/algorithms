def lowhigh(arr):
    low=arr[0]
    high=arr[0]
    for i in range (len(arr)):
	if arr[i]>high:
	    high=arr[i]
	elif arr[i]<low:
	    low=arr[i]
    print low
    return high



if __name__ == '__main__':
   print(lowhigh([40]))  
