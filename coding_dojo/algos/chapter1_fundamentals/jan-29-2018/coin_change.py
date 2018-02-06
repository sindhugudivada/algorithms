def coinchange(cents):
    pennies=0
    nickels=0
    dimes=0
    quarters=0
    amount=[]
    while cents > 0:
        if cents > 25:
	   cents=cents-25
	   quarters=quarters+1
	elif cents >10:
	    cents=cents-10
	    dimes=dimes+1
	elif cents > 5:
	    cents=cents-5
	    nickels=nickels+1
	elif cents >=1:
	    cents=cents-1
	    pennies=pennies+1

'print "{}:quarters,{}:dimes,{}:nickels,{}:pennies".format(quarters,dimes,nickels,pennies)'
amount.append(quarters)
amount.append(dimes)
amount.append(nickels)
amount.append(pennies)
print amount


if __name__=='__main__':
    coinchange(95)
