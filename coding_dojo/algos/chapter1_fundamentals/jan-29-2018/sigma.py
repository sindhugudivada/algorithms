def sigma(num):
    sum=0
    for i in range(0,num+1):
	sum=sum+i
    return sum


if __name__=='__main__':
    print(sigma(3))
