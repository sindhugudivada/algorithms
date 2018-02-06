def integers():
    count=0
    for i in range(1,256):
	count=count+i
	print "value:"+str(i)+" ,total:"+str(count)
    

if __name__=='__main__':
    integers()
