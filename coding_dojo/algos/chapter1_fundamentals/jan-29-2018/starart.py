def drawleftstars(num):
    st=""
    for i in range(0,num+1):
	st='*'*i
    print st	
    for i in range(num,75-num+1):
	st=" "*i
    return st	
def drawrightstars(num):
    st=""
    for i in range(0,num+1):
	st=' '*i
    print st
    for i in range(num,75-num+1):
	st='*'*i
    return st	



if __name__=='__main__':
    print(drawleftstars(10))
    print(drawrightstars(15))
