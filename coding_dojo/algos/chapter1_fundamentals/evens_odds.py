def evensodds(arr):
    count=0
    count1=0
    for i in range (len(arr)):
	if arr[i]%2==1:
	    count=count+1
	    if count==3:
		return "Thats odd"
        

if __name__ == '__main__':
    print(evensodds([2,3,8,7,5,2,8]) )
