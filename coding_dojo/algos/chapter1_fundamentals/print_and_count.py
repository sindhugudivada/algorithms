def integermultiples():
    count=0
    for x in range(512,4096):
	if x % 5 == 0:
	    print x,
	    count=count+1
    print count	    

if __name__ == '__main__':
   integermultiples()  
