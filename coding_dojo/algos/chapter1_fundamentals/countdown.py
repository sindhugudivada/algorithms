def countdown(number):
    arr=[] 
    while(number>=0):
	arr.append(number)
	number=number-1
    return arr

if __name__ == '__main__':
   print(countdown(5))  
