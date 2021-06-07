class Node:
    def __init__(self,data=0):
        self.next=None
        self.data=data

class CircularLinkedList:
    def __init__(self):
        self.head=None

    def insertBegin(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            newNode.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=newNode
            newNode.next=self.head
            self.head=newNode

    def insertEnd(self,data):
        newNode=Node(data)
        temp=self.head
        while temp.next!=self.head:  temp=temp.next
        temp.next=newNode
        newNode.next=self.head

    def insertMiddle(self,data,position):
        newNode=Node(data)
        temp=self.head
        for i in range(1,position): temp=temp.next

        newNode.next=temp.next
        temp.next=newNode

    def deleteEnd(self):
        temp=self.head
        prev=temp
        while temp.next!=self.head:
            prev=temp
            temp=temp.next
        print("Deleted element is",temp.data)
        prev.next=self.head
        del temp

    def deleteBegin(self):
        temp=self.head
        self.head=self.head.next
        temp.next=None
        trav=self.head
        while trav.next!=temp: trav=trav.next
        trav.next=self.head
        del temp    

    def display(self):
        temp=self.head
        while temp.next!=self.head:
            print(temp.data,end='   ')
            temp=temp.next
        print(temp.data)

    def deleteMiddle(self,position):
        temp=self.head
        prev=temp
        for i in range(1,position):
            prev=temp
            temp=temp.next
        prev.next=temp.next
        temp.next=None
        del temp
        

def main():
    print("Circular Linked List")
    c=CircularLinkedList()
    run=True
    while run:
        print("1.Insert Begin")
        print('2.Insert End')
        print('3.Insert Midddle')
        print("4.Display")
        print('5.Delete Begin')
        print('6.Delete End')
        print('7.Delete Middle')
        print('Any other character to exit')
        print("Enter the choice")
        ch=int(input())
        if ch==1:
            data=int(input('Enter the data'))
            c.insertBegin(data)
        elif ch==2:
            data=int(input('Enter the data'))
            c.insertEnd(data)
        elif ch==3:
            data=int(input('Enter the data'))
            pos=int(input("Enter the position"))
            c.insertMiddle(data,pos)
        elif ch==4:
            c.display()
        elif ch==5:
            c.deleteBegin()
        elif ch==6:
            c.deleteEnd()
        elif ch==7:
            pos=int(input('Enter the position'))
            c.deleteMiddle(pos)
        else:
            run=False
        print('\n')

if __name__=='__main__':
    main()
