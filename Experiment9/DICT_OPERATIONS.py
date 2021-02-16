def inert(my_dict):
    k=int(input("Enter key: "))
    v=(input("Enter value: "))
    my_dict[k]=v
    
def delete(my_dict):
    no=int(input("Enter a key to delete:"))
    del my_dict[no]
def search(my_dict):
    target=int(input("Enter a key to search: "))
    print(my_dict[target])
def display(my_dict):
    print(my_dict)
    
my_dict={1: 'apple', 2: 'ball'}
print("MENU OPTIONS")
print("1.INSERT\t2.DELETE\t3.SEARCH\t4.DISPLAY\t5.EXIT")
while(1):
    n = int(input("ENTER YOUR CHOICE: "))
    if n==1:
        inert(my_dict)
    elif n==2:
        delete(my_dict)
    elif n==3:
        search(my_dict)
    elif n==4:
        display(my_dict)
    elif n==5:
         break
    else :
        print("INVALID OPTION")





