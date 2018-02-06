def oneanother(arr):
    j=len(arr)-2
    value=arr[j]
    for i in range (len(arr)):
	if arr[i]%2 != 0:
	    oddvalue=arr[i]
	    print value
	    return oddvalue


if __name__ == '__main__':
   print(oneanother([40,13,5,9]))  
