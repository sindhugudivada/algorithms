def fitvalue(arr):
    if arr[0] > len(arr):
	print "Too big!"
    elif arr[0]<len(arr):
	print "Too small!"
    else:
	print "just right"

if __name__ == '__main__':
   fitvalue([2,5,7]) 
