def lengthvalues(number1,number2):
    arr=[]
    for i in range(0,number1):
	if (number1==number2):
	    print "Jinx!"
	else:    
	    arr.append(number2)
    return arr

if __name__ == '__main__':
   print(lengthvalues(7,2) ) 
