def collatz_sequence(number):
    sequence=[]
    while (number>1):
	if number % 2==0:
	    number=number/2
	    sequence.append(number)
	elif number % 2 == 1:
	    number=3*number+1
	    sequence.append(number)
    return sequence
	


if __name__=='__main__':
    print(collatz_sequence(13))

