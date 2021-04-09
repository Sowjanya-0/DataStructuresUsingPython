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
print("1.Push 2.Pop 3.Search 4.Display 5.Exit")
n = int(input("please enter a choice: "))
while(n>0):
    if n==1: 
        e=str(input("Enter any alphabet: "))
        push(e)
        print("1.Push 2.Pop 3.Search 4.Display 5.Exit")
        n = int(input("please enter a choice: "))
    elif n==2: 
        pop()
        print("1.Push 2.Pop 3.Search 4.Display 5.Exit")
        n = int(input("please enter a choice: "))
    elif n==3:
        k = str(input("Enter a key: "))
        search(k)
        print("1.Push 2.Pop 3.Search 4.Display 5.Exit")
        n = int(input("please enter a choice: "))
    elif n==4:
        display()
        print("1.Push 2.Pop 3.Search 4.Display 5.Exit")
        n = int(input("please enter a choice: "))
    elif n==5:
        exit()
    else: 
        print("Enter 1-4 only")
        print("1.Push 2.Pop 3.Search 4.Display 5.Exit")
        n = int(input("please enter a choice: "))
    