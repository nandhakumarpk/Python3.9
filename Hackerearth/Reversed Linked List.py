class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def insert(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
            
    def output(self):
        stack=[]
        temp=self.head
        while temp:
            if temp.data %2 == 0:
                run=temp
                while run and run.data%2==0:
                    stack.append(run.data)
                    run=run.next
                while stack:
                    print(stack.pop(),end=' ')
                temp=run
            else:
                print(temp.data,end=' ')
                temp=temp.next

n=int(input())
arr=[int(i) for i in input().split()]
s=SinglyLinkedList()
for i in arr:
    s.insert(i)
s.output()
