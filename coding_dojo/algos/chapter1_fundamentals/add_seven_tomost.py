def seventomost(arr):
    newarr=[]
    for i in range (1,len(arr)):
	    newarr.append(arr[i]+7)    
    return newarr



if __name__ == '__main__':
   print(seventomost([2,5,9,19]))  
