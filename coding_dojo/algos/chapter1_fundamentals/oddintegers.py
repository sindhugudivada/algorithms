def oddintegers():
    count=0
    for x in range(-300000,300000):
	if x%2 == 1:
	    count=count+x
    print count


if __name__ == '__main__':
   oddintegers()  
