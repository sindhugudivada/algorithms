def negative(arr):
    newarr=[]
    for i in range (len(arr)):
	if arr[i]>0:
	    newarr.append(arr[i]*-1)
	else:
	    newarr.append(arr[i])
    return newarr



if __name__ == '__main__':
   print(negative([2,5,-9,19]))  
