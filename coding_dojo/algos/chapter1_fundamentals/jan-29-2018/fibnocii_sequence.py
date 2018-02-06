def fibnocii_sequence(number):
    a=0
    b=1
    series=[0,1]
    for i in range(2,number):
	c=a+b
	a=b
	b=c
	series.append(c)
    return series
	


if __name__=='__main__':
    print(fibnocii_sequence(13))

