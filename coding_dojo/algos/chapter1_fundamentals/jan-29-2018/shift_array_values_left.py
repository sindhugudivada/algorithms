def eachvalue(arr):
    for i in range(0,len(arr)-2):
	arr[i]=arr[i+1]
    arr.append(0)
    return arr


if __name__=='__main__':
    print(eachvalue([6,7,8,9,10]))
