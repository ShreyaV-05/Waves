fr = input("Enter your first input: ")
se = input("Enter your second input: ")
th = input("Enter your third input: ")
fo = input("Enter your fourth input: ")
fi = input("Enter your fifth input: ")
inp=[fr,se,th,fo,fi]
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
for y in string:#if string find lenth of each string and sort depending on length
    #if char find ascii value and sort depending on asci value
