def is_prime(number):
    for i in range(2,number+1):
        if number%i== 0 and i!=number:
	   return "is not prime"
	else:
	    return "is prime"

if __name__=='__main__':
    print(is_prime(13))
    print(is_prime(6))
