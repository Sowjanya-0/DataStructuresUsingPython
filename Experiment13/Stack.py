#Initial Stack 
stack = ['x','y','z']

# Stack Insertion
def push(item):
    stack.append(item)
    
# Stack Display
def display():
    print(stack)

#Stack Deletion  
def pop():
    print(stack.pop())

#Stack Searching Operation
def search(key):
    flag =0
    for i in range (0,len(stack)) :
        if (stack[i]==key):
            print("\nFound at index "+str(i))
        else:
            flag=flag +1
        if (flag==len(stack) ):
            print("\nKey not present")
            
    
print("Menu Option")
while(1):
    print("1.Push 2.Pop 3.Search 4.Display 5.Exit")
    n = int(input("please enter a choice: "))
    if n==1: 
        e=str(input("Enter any alphabet: "))
        push(e)
    elif n==2: 
        pop()
    elif n==3:
        k = str(input("Enter a key: "))
        search(k)
    elif n==4:
        display()
    elif n==5:
        exit()
    else: 
        print("Enter 1-4 only")
