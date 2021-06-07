class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.__head=None

    def insertBegin(self,data):
        newNode=Node(data)
        if self.__head==None:
            self.__head=newNode
        else:
            newNode.next=self.__head
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

    def insertMiddleByPosition(self,data,position):
        newNode=Node(data)
        temp=self.__head
        for i in range(1,position):
            temp=temp.next
        newNode.next=temp.next
        temp.next=newNode

    def insertMiddleByValue(self,data,value):
        newNode=Node(data)
        temp=self.__head
        while(temp!=None and temp.data!=value):
            temp=temp.next
        newNode.next=temp.next
        temp.next=newNode

    def display(self):
        temp=self.__head
        while temp.next!=None:
            print(temp.data,end='->')
            temp=temp.next
        print(temp.data)

    def deleteBegin(self):
        temp=self.__head
        self.__head=self.__head.next
        temp.next=None
        return temp
    
    def deleteEnd(self):
        current=self.__head
        previous=current
        while current.next!=None:
            previous=current
            current=current.next
        previous.next=None
        return current

    
    def deleteMiddleByPosition(self,position):
        previous=current=self.__head
        for i in range(position):
            previous=current
            current=current.next
        previous.next=current.next
        current.next=None
        return current

    
    def deleteMiddleByValue(self,value):
        current=self.__head
        previous=current
        if self.__head.data==value:
            temp=self.__head
            self.__head=self.__head.next
            return temp
        while current.data!=value and current!=None:
            previous=current
            current=current.next
        if current==None:
            return "Value is not found"
        else:
            previous.next=current.next
            current.next=None
            return current

        
    def search(self,key):
       temp=self.__head
       i=1
       while temp!=None:
           if temp.data==key:
               print("Value found at",i,'position')
               return temp
           temp=temp.next
       print('Key not found')
       return None

        
    def updateBegin(self,newdata):
        if self.__head==None or self.__head.data==newdata:
            return False
        else:
            self.__head.data=newdata
            return True

    def updateEnd(self,newdata):
        if self.__head==None:
            return False
        else:
            temp=self.__head
            while(temp.next!=None):
                temp=temp.next
            if temp.data==newdata:
                return False
            else:
                temp.data=newdata
                return True

    def updateMiddleByPosition(self,newdata,position):
        if self.__head==None:
            return False
        else:
            temp=self.__head
            for i in range(1,position):
                if temp==None:
                    print("The position is out of bound")
                    return False
                temp=temp.next
            if temp.data==newdata:
                return False
            else:
                temp.data=newdata
                return True

    def updateMiddleByValue(self,newdata,value):
        if self.__head==None:
            return False
        else:
            temp=self.__head
            while temp!=None and temp.data!=value:
                temp=temp.next
            if temp==None:
                print("Value is not found")
                return False
            else:
                if temp.data==newdata:
                    return False
                else:
                    temp.data=newdata
                    return True

    def reverse(self):
        temp=self.__head
        reverse=None
        while temp!=None:
            node=Node(temp.data)
            node.next=reverse
            reverse=node
            temp=temp.next
        while reverse.next!=None:
            print(reverse.data,end='->')
            reverse=reverse.next
        print(reverse.data)
        return reverse        

    def sort(self):
        temp=self.__head
        arr=[]
        while temp!=None:
            arr.append(temp.data)
            temp=temp.next
        n=len(arr)
        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        temp=self.__head
        for i in range(n):
            temp.data=arr[i]
            temp=temp.next

def main():
    s=SinglyLinkedList()
    print("SINGLE LINKED LIST")
    print('********************************************')
    while True:
        print('1.Insert in the beginnning')
        print('2.Insert in the End')
        print('3.Insert in the Middle by Position')
        print('4.Insert in the Middle by value')
        print('5.Display')
        print('6.Deletion in Beginning')
        print('7.Deletion in End')
        print('8.Deletion in the Middle by Position')
        print('9.Deletion in the Middle by value')
        print('10.Search')
        print('11.Update in the Beginning')
        print('12.Update in the End')
        print('13.Update in the Middle by Position')
        print('14.Update in the Middle by value')
        print('15.Reverse')
        print('16.Sort')
        print('Enter any other number to exit')
        print("********************************************")
        ch=int(input('Enter your choice\n'))
        if ch>=1 and ch<=4:
            data=int(input("Enter the data\n"))
            if ch==1:
                s.insertBegin(data)
            elif ch==2:
                s.insertEnd(data)
            elif ch==3:
                position=int(input("Enter the position\n"))
                s.insertMiddleByPosition(data,position)
            elif ch==4:
                value=int(input("Enter the value\n"))
                s.insertMiddleByValue(data,value)
        elif ch==5:
            s.display()
        elif ch==6:
            print(s.deleteBegin())
        elif ch==7:
            print(s.deleteEnd())
        elif ch==8:
            position=int(input("Enter the position\n"))
            print(s.deleteMiddleByPosition(position))
        elif ch==9:
            value=int(input("Enter the value\n"))
            print(s.deleteMiddleByValue(value))
        elif ch==10:
            key=int(input("Enter the key\n"))
            print(s.search(key))
        elif ch>=11 and ch<=14:
            newdata=int(input('Enter the new data\n'))
            if ch==11:
                print(s.updateBegin(newdata))
            elif ch==12:
                print(s.updateEnd(newdata))
            elif ch==13:
                position=int(input("Enter the position\n"))
                print(s.updateMiddleByPosition(newdata,position))
            elif ch==14:
                value=int(input("Enter the value\n"))
                print(s.updateMiddleByValue(newdata,value))
        elif ch==15:
            print(s.reverse())
        elif ch==16:
            s.sort()
        else:
            return
        print('\n')
if __name__=='__main__':
    main()
