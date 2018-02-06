def drawleftchars(num,char):
    st=""
    space=75-num
    for i in range(0,num):
	st=st+char
    while space>0:
	st=st+""
	space=space-1
    return st	

def drawrightchars(num,char):
    st=""
    space=75-num
    while space>0:
	st=st+""
	space=space-1
    for i in range (0,num):
	st=st+char
    return st


if __name__=='__main__':
    print(drawleftchars(30,"&"))

    print(drawrightchars(30,"%"))
