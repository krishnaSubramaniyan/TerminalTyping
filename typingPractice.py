import os,random;


print("\n"+"\033[94m"+"TYPING PRACTICE".center(os.get_terminal_size().columns)+"\033[00m")

#data
Correct = ('good','nice','execellent','high quality','Geate','Groovy','Sweet')
Wrong = ('better','lousy','unexpected','unacceptable')

Para = (
('ask', 'fad', 'alas', 'asks', 'shad', 'lads', 'flags', 'flask', 'glass', 'jag', 'fag', 'fall', 'hash', 'glad', 'sags', 'galls', 'halls', 'salad', 'jak', 'has', 'jags', 'gaff', 'hall', 'dash', 'flask', 'slash', 'flasks', 'lad', 'sad', 'lash', 'adds', 'gall', 'gash', 'shall', 'lakhs', 'dhalls'),
    
('lad', 'sad', 'lash', 'adds', 'gall', 'gash', 'shall', 'lakhs', 'dhalls', 'jak', 'has', 'jags', 'gaff', 'hall', 'dash', 'flask', 'slash', 'flasks', 'jag', 'fag', 'fall', 'hash', 'glad', 'sags', 'galls', 'halls', 'salad', 'ask', 'fad', 'alas', 'asks', 'shad', 'lads', 'flags', 'flask', 'glass'),

    ('awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;'),

)

Para = (
    (
        ('ask', 'fad', 'alas', 'asks', 'shad', 'lads', 'flags', 'flask', 'glass'), 
        ('jag', 'fag', 'fall', 'hash', 'glad', 'sags', 'galls', 'halls', 'salad'), 
        ('jak', 'has', 'jags', 'gaff', 'hall', 'dash', 'flask', 'slash', 'flasks'), 
        ('lad', 'sad', 'lash', 'adds', 'gall', 'gash', 'shall', 'lakhs', 'dhalls')
    ),
    (
        ('lad', 'sad', 'lash', 'adds', 'gall', 'gash', 'shall', 'lakhs', 'dhalls'),
        ('jak', 'has', 'jags', 'gaff', 'hall', 'dash', 'flask', 'slash', 'flasks'), 
        ('jag', 'fag', 'fall', 'hash', 'glad', 'sags', 'galls', 'halls', 'salad'), 
        ('ask', 'fad', 'alas', 'asks', 'shad', 'lads', 'flags', 'flask', 'glass')
    ),
    (
        ('awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;'),
        ('awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;'),
        ('awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;'),
        ('awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;'),
        ('awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;', 'awerqfa', ';oiupj;')
    ),
    (
        ('fish', 'kodak', 'ahead', 'larks', 'quail', 'apples', 'reader', 'flukes', 'fiddle'), 
        ('dead', 'rails', 'sales', 'agile', 'isles', 'should', 'liquid', 'shower', 'saddle'), 
        ('idols', 'jaded', 'sails', 'filed', 'legal', 'folder', 'sledge', 'squall', 'larger'), 
        ('grade', 'jails', 'lakes', 'roses', 'rupee', 'squeal', 'fields', 'lulled', 'dislike'),
        ('apple', 'dirks', 'lease', 'equip', 'skill', 'easels', 'dollar', 'poorer', 'require'),
        ('asked', 'forks', 'hedge', 'would', 'grass', 'jokers', 'jailer', 'equals', 'refresh'),
        ('fails', 'usual', 'liked', 'walks', 'peaks', 'orders', 'follow', 'drawls', 'defiles')
    ),
    (
        ('lawyers', 'streaks', 'shipped', 'hillside', 'herewith', 'proposals'),
        ('shekels', 'forward', 'desired', 'loophole', 'jugglers', 'strapples'),
        ('hatless', 'figures', 'prepare', 'feathery', 'freehold', 'struggles'),
        ('thought', 'thyself', 'treated', 'assessed', 'prepared', 'territory'),
        ('quarter', 'yodlers', 'youthful', 'although', 'supplies', 'guileless'),
        ('freight', 'further', 'plougher', 'shippers', 'slightly', 'telegraph'),
        ('dutiful', 'pleased', 'goodwill', 'tortuous', 'property', 'addressed'),
        ('laughed', 'kettles', 'whiskers', 'thorough', 'repeated', 'flashlight'),
        ('petrols', 'regular', 'equipped', 'lilliput', 'etiquette', 'powerfully'),
        ('without', 'waggish', 'laughter', 'kirkwall', 'yesterday', 'typewriter')
     )
)

LineCount = (
    ( 4 , 9 ),
    ( 4 , 9 ),
    ( 5 , 8 ),
    ( 7 , 9 ),
    ( 10 , 6 )
)

PrintPara = (
    "ask fad alas asks shad lads flags flask glass\njag fag fall hash glad sags galls halls salad\njak has jags gaff hall dash flask slash flasks\nlad sad lash adds gall gash shall lakhs dhalls",

    "lad sad lash adds gall gash shall lakhs dhalls\njak has jags gaff hall dash flask slash flasks\njag fag fall hash glad sags galls halls salad\nask fad alas asks shad lads flags flask glass",

    "awerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj;\nawerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj;\nawerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj;\nawerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj;\nawerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj;",

    'fish kodak ahead larks quail apples reader flukes fiddle\ndead rails sales agile isles should liquid shower saddle\nidols jaded sails filed legal folder sledge squall larger\ngrade jails lakes roses rupee squeal fields lulled dislike\napple dirks lease equip skill easels dollar poorer require\nasked forks hedge would grass jokers jailer equals refresh\nfails usual liked walks peaks orders follow drawls defiles',

    'lawyers streaks shipped hillside herewith proposals\nshekels forward desired loophole jugglers strapples\nhatless figures prepare feathery freehold struggles\nthought thyself treated assessed prepared territory\nquarter yodlers youthful although supplies guileless\nfreight further plougher shippers slightly telegraph\ndutiful pleased goodwill tortuous property addressed\nlaughed kettles whiskers thorough repeated flashlight\npetrols regular equipped lilliput etiquette powerfully\nwithout waggish laughter kirkwall yesterday typewriter'

)


#MainLoop
while(True):
#print para
    print("\n\n\nprint this paragraph\n")
    #GetPara = random.randint(0,(len(Para)-1))
    GetPara = 3;
    print(PrintPara[GetPara],"\n")


    #input
    typeData = []
    j = LineCount[GetPara][0]
    k = 0

    while(j != 0):
        temp = input()
        if(temp == ""):
            break
        
        SplitString = temp.strip().split(" ")
        typeData.append(list())
        for i in range(len(SplitString)):
            typeData[k].append(SplitString[i])
        k += 1
        j -= 1


    #validation
    if(not typeData):
        print("empty")
    
    else:
        wronglyTypedWordsIndex = [];
        noAnotherError = True
        wrongCount = 0
        print(" ")
        for i in range(LineCount[GetPara][0]):
            try:
                length = len(typeData[i])
                if(LineCount[GetPara][1] > len(typeData[i])):
                    print("line",i+1,"are not fully typed :|")
                    noAnotherError = False

                
                elif(LineCount[GetPara][1] < len(typeData[i])):
                    print("line",i+1,"extra typed :|")
                    length = LineCount[GetPara][1]
                    noAnotherError = False
                
                for j in range(length):
                    if(Para[GetPara][i][j] != typeData[i][j]):
                        wrongCount+=1
                        wronglyTypedWordsIndex.append([i,j]);
                        
            except IndexError:
                print("line",i+1,"not typed :|")


        #score session
        print("\n")
        if(wrongCount == 0 and noAnotherError):
            print("\033[32m"+Correct[random.randint(0,len(Correct)-1)].upper()+"\033[00m")
        
        else:
            pointer = 0;
            if(wrongCount < 4 ):
                print("\033[31m"+Wrong[wrongCount-1].upper()+"\033[00m")
            else:
                print("\033[31m"+Wrong[3].upper()+"\033[00m")

            print("wrong count = ",wrongCount,"\n")
            for i in range(len(typeData)):
                for j in range(len(typeData[i])):
                    if(pointer < len(wronglyTypedWordsIndex) and wronglyTypedWordsIndex[pointer][0] == i and wronglyTypedWordsIndex[pointer][1] == j):
                        print("\033[31m"+typeData[i][j]+"\033[00m", end=" ")
                        pointer += 1;
                    else:
                        print(typeData[i][j],end=" ")
                print("")



    #loop end condition
    temp2 = input("\n\nyou will continue? (press enter to continue) ")
    if(temp2 == ""):
        continue
    else:
        break
