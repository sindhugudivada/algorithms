def MakeItBig(arr):
    for i in range (len(arr)):
	if arr[i]>0:
	    arr[i]="big"
    return arr	    

if __name__ == '__main__':
   print(MakeItBig([-1,3,5,-5]))  
