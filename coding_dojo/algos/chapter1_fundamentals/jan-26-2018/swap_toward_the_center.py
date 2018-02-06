def swaptowardcenter(arr):
    for i in range(len(arr)/2):
	if i%2 == 0:
	    temp=arr[i]
	    arr[i]=arr[len(arr)-1-i]
	    arr[len(arr)-1-i]=temp
    return arr

if __name__=='__main__':
    print(swaptowardcenter(["true",42,"ada",2,"pizza"]))
