def stringforarray(arr):
    for i in range(len(arr)):
	if arr[i]<0:
	    arr[i]='DOJO'

    return arr


if __name__=='__main__':
    print stringforarray([1,-3,4,-5,6,7,-9])
