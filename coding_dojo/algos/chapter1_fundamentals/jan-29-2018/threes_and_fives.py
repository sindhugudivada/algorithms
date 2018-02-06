def threesandfives(start,end):
    sum=0
    for i in range(start,end+1):
	sum=sum+i
    if sum %3==0 or sum%5==0:
	print sum



if __name__=='__main__':
    threesandfives(100,4000000)
