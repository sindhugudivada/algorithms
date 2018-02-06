def max_min_average(arr):
    max=arr[0]
    min=arr[0]
    avg=0
    medium=0
    for i in range (len(arr)):
	if arr[i]>max:
	    max=arr[i]
	elif arr[i]<min:
	    min=arr[i]
	avg=(avg+arr[i])
    medium=avg/len(arr)
    print max,min,medium

if __name__=='__main__':
    max_min_average([1,2,3,4,5,6,7,8,9])
