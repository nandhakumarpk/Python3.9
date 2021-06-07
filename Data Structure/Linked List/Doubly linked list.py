class Node:
    def __init__(self,data=0):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLinedList:
    def __init__(self):
        self.__head=None

    def insertBegin(self,data):
        newNode=Node(data)
        if self.__head==None:
            self.__head=newNode
        else:
            newNode.next=self.__head
            self.__head.prev=newNode
            self.__head=newNode

    def insertEnd(self,data):
        newNode=Node(data)
        if self.__head==None:
            self.__head=newNode
        else:
            temp=self.__head
            while temp.next!=None:
                temp=temp.next

            temp.next=newNode
            newNode.prev=temp

    def insertMiddle(self,data,position):
        newNode=Node(data)
        temp=self.__head
        for i in range(1,position):
            temp=temp.next

        newNode.next=temp.next
        newNode.prev=temp
        temp.next=newNode

    def deleteBegin(self):
        temp=self.__head
        self.__head=self.__head.next
        temp.next=None
        #return temp

    def deleteEnd(self):
        current=self.__head
        prev=current
        while current.next!=None:
            prev=current
            current=current.next
        prev.next=None
        current.prev=None
        #return current
        
    def deleteMiddle(self,position):
        previous =self.__head
        current = self.__head
        for i in range(1,position):
            previous=current
            current=current.next
        previous.next=current.next
        previous.next.prev=previous
        current.next=None
        current.prev=None
        #return current

    def display(self):
        temp=self.__head
        while temp.next!=None:
            print(temp.data,end='->')
            temp=temp.next
        print(temp.data)
        
    def search(self):
        temp=self.__head
        key=int(input("Enter the key\n"))
        i=1
        while temp!=None:
            if temp.data==key:
                print("Key found at",i,'position')
                return
            temp=temp.next
            i+=1
        print("Key is not found")

    def bubble(self,arr):
        n=len(arr)
        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j]>arr[j+1]: arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr

    def sort(self):
        temp=self.__head
        arr=[]
        while temp!=None:
            #print(temp.data)
            arr.append(temp.data)
            temp=temp.next
        #arr.append(temp.data)
        arr=self.bubble(arr)
        temp=self.__head
        for i in range(len(arr)):
            temp.data=arr[i]
            temp=temp.next
def main():
    print("DOUBLY LINKED LIST")
    c=DoublyLinedList()
    run=True
    while run:
        print("******************************************")
        print("1.Insert Begin")
        print('2.Insert End')
        print('3.Insert Midddle')
        print("4.Display")
        print('5.Delete Begin')
        print('6.Delete End')
        print('7.Delete Middle')
        print('8.Search')
        print('9.Sort')
        print('Any other number to exit')
        print("******************************************")
        print("Enter the choice")
        ch=int(input())
        if ch==1:
            data=int(input('Enter the data\n'))
            c.insertBegin(data)
        elif ch==2:
            data=int(input('Enter the data\n'))
            c.insertEnd(data)
        elif ch==3:
            data=int(input('Enter the data\n'))
            pos=int(input("Enter the position\n"))
            c.insertMiddle(data,pos)
        elif ch==4:
            c.display()
        elif ch==5:
            c.deleteBegin()
        elif ch==6:
            c.deleteEnd()
        elif ch==7:
            pos=int(input('Enter the position\n'))
            c.deleteMiddle(pos)
        elif ch==8:
            c.search()
        elif ch==9:
            c.sort()
        else:
            run=False
        print('\n')

if __name__=='__main__':
    main()
