def finalcountdown(param1,param2,param3,param4):
    count=param2
    while(count<param3):
        if count % param1 == 0 and count !=param4:
            print count
	count=count+1

if __name__ == '__main__':
   finalcountdown(3,5,17,9)  
