fr = input("Enter your first input: ")
se = input("Enter your second input: ")
th = input("Enter your third input: ")
fo = input("Enter your fourth input: ")
fi = input("Enter your fifth input: ")
inp=[fr,se,th,fo,fi]
num=[]
string=[]
chara=[]
def find_type():
    for x in inp:#figure out what type of input
        if type(x) == int:
            num.append(x)
        if type(x) == str:
            string.append(x)
        if type(x) == chr:
            chara.append(x)
    bubblestringsort(string)
    bubblecharasort(chara)
    bubbleintsort(int)
    print ("Sorted input is:")
    for i in range(len(string)):
        print ("%d" %string[i])
    for i in range(len(string)):
        print ("%d" %string[i])
    for i in range(len(string)):
        print ("%d" %string[i])

"""
for y in string: #if string find length of each string and sort depending on length
    z = len(y)
    sort.append(z)
for u in chara: #if char find ascii value and sort depending on asci value
    v = sort.append(ord(u))
"""
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
            if sort[len(j)] > sort[len(j+1)] :
                sort[len(j)], sort[len(j+1)] = sort[len(j+1)], sort[len(j)]
def bubblecharasort(sort):
    n=len(sort)
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if sort[ord(j)] > sort[ord(j+1)] :
                sort[ord(j)], sort[ord(j+1)] = sort[ord(j+1)], sort[ord(j)]
