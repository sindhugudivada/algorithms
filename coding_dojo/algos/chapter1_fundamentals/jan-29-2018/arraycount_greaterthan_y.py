def array_count(arr,y):
    count=0
    for i in range (len(arr)):
	if arr[i]>y:
	    count=count+1
    print count

if __name__=='__main__':
    array_count([1,2,3,4,5,6,7,8,9],4)
