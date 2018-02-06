def countpositives(arr):
    count=0
    for i in range (len(arr)):
	if arr[i]>0:
	    count=count+1
    arr[i]=count
    return arr


if __name__ == '__main__':
   print(countpositives([-2]))  
