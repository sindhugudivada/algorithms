def reversearray(arr):
    for i in range (len(arr)/2):
	temp=arr[i]
	arr[i]=arr[len(arr)-1-i]
	arr[len(arr)-1-i]=temp
    return arr



if __name__ == '__main__':
   print(reversearray([2,5,9,19,20]))  
