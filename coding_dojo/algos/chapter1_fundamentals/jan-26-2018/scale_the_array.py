def scalearray(arr,num):
    newarr=[]
    for i in range(len(arr)):
	newarr.append(arr[i]*num)
    return newarr

if __name__=='__main__':
    print(scalearray([1,2,3,4,5,6],5))
