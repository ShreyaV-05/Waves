def find_type(inp):
    num=[]
    string=[]
    chara=[]
    for x in inp:#figure out what type of input
        if type(x) == int:
            num.append(x)
        if type(x) == str:
            string.append(x)
        if type(x) == chr:
            chara.append(x)
    bubblestringsort(string)
    bubblecharasort(chara)
    bubbleintsort(num)

def bubbleintsort(sort):
    n=len(sort)
    # Traverse through all array elements
    for i in range(n-1):
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
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if len(sort[j]) > len(sort[j+1]):
                sort[j], sort[j+1] = sort[j+1], sort[j]
def bubblecharasort(sort):
    n=len(sort)
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if ord(sort[j]) > ord(sort[j+1]) :
                sort[j], sort[j+1] = sort[j+1], sort[j]
fr = input("Enter your first input: ")
se = input("Enter your second input: ")
th = input("Enter your third input: ")
fo = input("Enter your fourth input: ")
fi = input("Enter your fifth input: ")
inp=[fr,se,th,fo,fi]
find_type(inp)





