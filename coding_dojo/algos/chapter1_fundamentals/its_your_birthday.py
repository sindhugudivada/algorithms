def print_and_count(start, end):
   for i in xrange(start, end):
       if i%5  == 0:
	   print i,

if __name__ == '__main__':
        print_and_count(512,4096)
