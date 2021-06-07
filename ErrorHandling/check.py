try:
    class checking:
        
        def test_check(test_cases):
            if 0<test_cases<106:
                return True
            else:
                return False
                
        def event_check(a,b):
            if a!=b and a<b:
                return True
            else:
                return False

    class events:
        
        def __init__(self,test_cases):
            self.lis=[]
            self.test_cases=test_cases
            self.result=0
            self.temp=0
            
        def events_in_range(self):
            for i in range(self.test_cases):
                a,b=map(int,input().split())
                if checking.event_check(a,b):
                    self.lis.append([a,b])
                else:
                    print('Invalid input')
                    exit()
            self.lis.sort()
            self.temp=self.lis[0][1]
            for i in range(1,test_cases):
                if self.lis[i][1]<=self.temp:
                    self.result+=1
                else:
                    self.temp=self.lis[i][1]
    
        def __repr__(self):
            return '%d'%(self.result)

    if __name__=='__main__':
        test_cases=int(input('Enter number of events: '))
        if checking.test_check(test_cases):
            print('Enter events:\n')
            event_1=events(test_cases)
            event_1.events_in_range()
            print(event_1)
        else:
            print('Enter test cases between 1 and 105')

except ValueError:
    print('Invalid input\nEnter integers only')

except:
    print('\t\t Error')
    print('--------Oops! Something went wrong--------')
    print('\t-----Please try again-----')
