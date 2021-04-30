def find_type():
    s='n'
    c='n'
    n='n'
    num=[]
    string=[]
    chara=[]
    s = input("Will you be inputting strings to bubble sort (type n for no and y for yes): ")
    c = input("Will you be inputting characters to bubble sort (type n for no and y for yes):")
    n = input("Will you be inputting integers to bubble sort (type n for no and y for yes):")
    if s != 'n':
        fr = input("Enter your first string: ")
        se = input("Enter your second string: ")
        th = input("Enter your third string: ")
        fo = input("Enter your fourth string: ")
        fi = input("Enter your fifth string: ")
        string=[fr,se,th,fo,fi]
        bubblestringsort(string)
        print(1)
        print(string)
    elif c != 'n':
            fr = input("Enter your first character: ")
            se = input("Enter your second character: ")
            th = input("Enter your third character: ")
            fo = input("Enter your fourth character: ")
            fi = input("Enter your fifth character: ")
            chara=[fr,se,th,fo,fi]
            bubblecharasort(chara)
            print(2)
            print(chara)
    elif n != 'n':
            fr = input("Enter your first integer: ")
            se = input("Enter your second integer: ")
            th = input("Enter your third integer: ")
            fo = input("Enter your fourth integer: ")
            fi = input("Enter your fifth integer: ")
            num=[fr,se,th,fo,fi]
            bubbleintsort(num)
            print(3)
            print(num)

def bubbleintsort(sort):
    n=len(sort)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if sort[j] > sort[j+1] :
                sort[j], sort[j+1] = sort[j+1], sort[j]
def bubblestringsort(sort):
    # Traverse through all array elements
    n=len(sort)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if len(sort[j]) > len(sort[j+1]):
                sort[j], sort[j+1] = sort[j+1], sort[j]
def bubblecharasort(sort):
    n=len(sort)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if ord(sort[j]) > ord(sort[j+1]) :
                sort[j], sort[j+1] = sort[j+1], sort[j]

find_type()





