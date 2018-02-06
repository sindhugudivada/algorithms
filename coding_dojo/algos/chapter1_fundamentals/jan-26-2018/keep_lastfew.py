def keeplastfew(arr,num):
    newarr=[]
    newarr.append(arr[-num:])
    print newarr

if __name__=='__main__':
    keeplastfew([1,9,2,3,4,5,6],3)
