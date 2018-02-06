from node import Node

def createlist(arr):
    dummy=Node(-1)
    current=dummy
    count=0
    for i in arr:
	current.next=Node(i)
	current=current.next
	count=count+1
    return (dummy.next,count)

def createarray(ll):
    head,count=ll
    arr=[0]*count
    while(head):
	arr[count-1]= head.data
	count=count-1
	head=head.next
    return arr

if __name__=='__main__':
   abc = createarray(createlist([1,2,3,4]))
   print abc
