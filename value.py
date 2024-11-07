import os;

def stringFormat(data):
    # validate
    wordCount = len(data[0]);
    sameWordCount = True;
    for i in range(len(data)):
        if(wordCount != len(data[i])):
            sameWordCount = False;

    if(sameWordCount):
        #find lengthy word each column
        largeWordsLength = [];
        #i for column
        #j for row
        for i in range(len(data[0])):
            for j in range(len(data)):
                if(j == 0):
                    largeWordsLength.append(len(data[j][i]));
                elif(len(data[j][i]) > largeWordsLength[i]):
                    largeWordsLength[i] = len(data[j][i]);

        #format string
        for i in range(len(largeWordsLength)):
            largeWordsLength[i] += 1;
        
        formatedString = ""
        for i in range(len(data)):
            for j in range(len(data[0])):
                formatedString += data[i][j].ljust(largeWordsLength[j]);
            formatedString += "\n"

        return repr(formatedString[:-2]);

    else:
        string = "";
        for i in range(len(data)):
            for j in range(len(data[i])):
                string += data[i][j]+" ";
            string += '\n';
        return repr(string[:-2]);

    
print("enter data")
temp = []
while(True):
    temp1 = input()
    if(temp1 == ""):
        break
    else:
        temp.append(tuple(temp1.split(" ")))

#print validation data
print(tuple(temp),"\n")

#print raw string(printable string)
print(stringFormat(temp));
