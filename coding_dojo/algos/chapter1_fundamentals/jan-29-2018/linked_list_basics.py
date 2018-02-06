from node import Node

def createlist(arr):
    dummy=Node(-1)
    current=dummy
    for i in arr:
	current.next=Node(i)
	current=current.next
    return dummy.next

def printlinkedlist(value):
    current=value
    while current:
	print current.data
	current=current.next
    


if __name__=='__main__':
   abc = createlist([1,2,3,4])
   printlinkedlist(abc)
