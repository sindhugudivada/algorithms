def doublevision(arr):
    arr1=[]
    for i in range (len(arr)):
	arr1.append(2*arr[i])
    return arr1



if __name__ == '__main__':
   print(doublevision([2,4,6,8]))  
