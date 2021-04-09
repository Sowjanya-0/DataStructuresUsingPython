#Initial Queue
queue = []

# EnQueue
def enqueue(item):
    queue.append(item)
    
# Stack Display
def display():
    print(queue)

# DeQueue  
def dequeue():
    print(queue.pop(0))

#Queue Searching Operation
def search(key):
    flag =0
    for i in range (0,len(queue)) :
        if (queue[i]==key):
            print("\nFound at index "+str(i))
        else:
            flag=flag +1
        if (flag==len(queue) ):
            print("\nKey not present")
            
    
print("Menu Option")
while(1):
    print("1.Enqueue 2.Dequeue 3.Search 4.Display 5.Exit")
    n = int(input("please enter a choice: "))
    if n==1: 
        e=str(input("Enter any alphabet: "))
        enqueue(e)
    elif n==2: 
        dequeue()
    elif n==3:
        k = str(input("Enter a key: "))
        search(k)
    elif n==4:
        display()
    elif n==5:
        exit()
    else: 
        print("Enter 1-4 only")

    
