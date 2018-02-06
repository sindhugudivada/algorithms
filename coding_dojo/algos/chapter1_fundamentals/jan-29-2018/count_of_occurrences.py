def count_of_occurences(str,letter):
    count=0
    for i in range (len(str)):
	if letter==str[i]:
	    count=count+1
    print count

if __name__=='__main__':
    count_of_occurences('abcdabcd','c')
