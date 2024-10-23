#data
leftHand = ('a','s','d','f','g','q','w','e','r','t','z','x','c','v','b');
rightHand = ('h','j','k','l',';','y','u','i','o','p','m','n');
data = [];
leftHandCount = 0;
rightHandCount = 0;
total = 0;

#input
print("enter paragraph");
while(True):
    temp = input();
    if(temp == ''):
        break
    else:
        data.append(temp);


#calculate
for i in range(len(data)):
    for letter in data[i]:
        if(letter == ' '):
            rightHandCount += 1;
        elif(letter in leftHand):
            leftHandCount += 1;
        elif(letter in rightHand):
            rightHandCount += 1;

total = leftHandCount + rightHandCount;

print("LETTER COUNT".center(60,"-"))
print("leftHand Count  = ",leftHandCount);
print("rightHand Count = ",rightHandCount);
print("total           = ",total);

print()
print("PERCENTAGE".center(60,"-"));
print(f"leftHand  = {(leftHandCount/total*100):.2f}%");
print(f"rightHand = {(rightHandCount/total*100):.2f}%");
