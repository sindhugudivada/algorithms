def factorial(num):
    product=1
    for i in range(2,num+1):
	product=product*i
    return product	



if __name__=='__main__':
    print(factorial(5))
