def firstvalue(arr):
    if(arr[0]!=int):
	total=0+len(arr)
    else:
	total=arr[0]+len(arr)
    return total

if __name__ == '__main__':
   print(firstvalue(["what",9,10])),
   print(firstvalue([100,9,10])),
