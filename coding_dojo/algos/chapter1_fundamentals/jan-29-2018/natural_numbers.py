def natural_numbers():
    sum=0
    for i in range(0,1000):
	if i%3==0 or i%5==0:
	   sum=sum+i  
    return sum


if __name__=='__main__':
    print natural_numbers()
