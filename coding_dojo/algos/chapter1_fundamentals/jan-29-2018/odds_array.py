def odds_array():
    arr=[]
    for i in range (1,256):
	if i%2==1:
	    arr.append(i)
    print arr

if __name__=='__main__':
    odds_array()
