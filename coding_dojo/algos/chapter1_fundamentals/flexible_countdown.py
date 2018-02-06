def flexicountdown(lowNum,highNum,mult):
    for x in range(lowNum,highNum+1):
        if x % mult == 0:
            print x 

if __name__ == '__main__':
   flexicountdown(2,9,3)  
