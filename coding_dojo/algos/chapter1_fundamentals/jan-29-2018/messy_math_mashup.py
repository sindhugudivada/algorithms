def messy_mashup(num):
    total=0
    for i in range(0,num):
        if i==num/3:
	    total=-1
	    break
	elif i%7==0:
	    total=2*i+total
	elif i%3==0:
	     continue
	else:    
	    total=total+i    
    print total
    return total

if __name__=='__main__':
    messy_mashup(4)
    messy_mashup(8)
    messy_mashup(15)
