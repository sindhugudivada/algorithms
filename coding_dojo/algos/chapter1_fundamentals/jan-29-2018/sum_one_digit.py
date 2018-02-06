def sum_to_one(number):
    value=str(number)
    while len(value)>1:
	total=0
	for i in value:
	    total=total+int(i)
	value=str(total)	
    return int(value)

if __name__=='__main__':
    print(sum_to_one(99999))
