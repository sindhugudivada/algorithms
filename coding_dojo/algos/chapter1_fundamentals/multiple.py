def multiples():    
    i=1
    while (i<60000):
	if (i % 6) == 0:
	    print i,
	i=i+6

if __name__ == '__main__':
   multiples()  
