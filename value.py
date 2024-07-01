import os;
print("enter data")
temp = []
string = ""
while(True):
    temp1 = input()
    if(temp1 == ""):
        break
    else:
        string+=temp1+"\n"
        temp.append(tuple(temp1.split(" ")))

os.system("clear")
print(tuple(temp),"\n")

print("(",len(temp),",",len(temp[0]),")\n")

print(repr(string)[:-3]+"'\n")