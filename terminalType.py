from tkinter import Tk,Label;
import os,random;

print("\n"+"\033[94m"+"TERMINAL TYPE".center(os.get_terminal_size().columns)+"\033[00m")

#data
Correct = ('good','nice','execellent','high quality','Geate','Groovy','Sweet')
Wrong = ('better','lousy','unexpected','unacceptable')

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
        ('gftfrf', 'hjyjuj', 'gftfrf', 'hjyjuj', 'gftfrf', 'hjyjuj', 'gftfrf', 'hjyjuj'),
        ('gftfrf', 'hjyjuj', 'gftfrf', 'hjyjuj', 'gftfrf', 'hjyjuj', 'gftfrf', 'hjyjuj'),
        ('gftfrf', 'hjyjuj', 'gftfrf', 'hjyjuj', 'gftfrf', 'hjyjuj', 'gftfrf', 'hjyjuj'),
        ('gftfrf', 'hjyjuj', 'gftfrf', 'hjyjuj', 'gftfrf', 'hjyjuj', 'gftfrf', 'hjyjuj'),
        ('gftfrf', 'hjyjuj', 'gftfrf', 'hjyjuj', 'gftfrf', 'hjyjuj', 'gftfrf', 'hjyjuj')
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
     ),
    (
        ('azxcvf', 'lkmnbj', 'azxcvf', 'lkmnbj', 'azxcvf', 'lkmnbj', 'azxcvf', 'lkmnbj'),
        ('azxcvf', 'lkmnbj', 'azxcvf', 'lkmnbj', 'azxcvf', 'lkmnbj', 'azxcvf', 'lkmnbj'),
        ('azxcvf', 'lkmnbj', 'azxcvf', 'lkmnbj', 'azxcvf', 'lkmnbj', 'azxcvf', 'lkmnbj'),
        ('azxcvf', 'lkmnbj', 'azxcvf', 'lkmnbj', 'azxcvf', 'lkmnbj', 'azxcvf', 'lkmnbj'),
        ('azxcvf', 'lkmnbj', 'azxcvf', 'lkmnbj', 'azxcvf', 'lkmnbj', 'azxcvf', 'lkmnbj')
    ),
    (
        ('amazed', 'journal', 'gambols', 'pickling', 'vineyard', 'grizzled'),
        ('except', 'jackets', 'fixture', 'austrian', 'appeared', 'frequent'),
        ('logical', 'student', 'spacing', 'movement', 'joyfully', 'premises'),
        ('sixfold', 'succeed', 'western', 'examined', 'accuracy', 'fortress'),
        ('daybook', 'lecture', 'neither', 'vexation', 'quantity', 'executor'),
        ('kindled', 'general', 'private', 'practice', 'question', 'deduction'),
        ('jingled', 'amulets', 'service', 'produces', 'requires', 'judicious'),
        ('jumbled', 'arrival', 'relative', 'provoked', 'starting', 'materials'),
        ('swivels', 'fizzed', 'possible', 'somewhat', 'cylinder', 'assessment'),
        ('violets', 'regaled', 'becoming', 'gracious', 'thousand', 'appearance')
    ),
    (
        ('abcdefghijklmnopqrstuvwxyz.,', 'zyxwvutsrqponmlkjihgfedcba.,'),
        ('abcdefghijklmnopqrstuvwxyz.,', 'zyxwvutsrqponmlkjihgfedcba.,'),
        ('abcdefghijklmnopqrstuvwxyz.,', 'zyxwvutsrqponmlkjihgfedcba.,'),
        ('abcdefghijklmnopqrstuvwxyz.,', 'zyxwvutsrqponmlkjihgfedcba.,'),
        ('abcdefghijklmnopqrstuvwxyz.,', 'zyxwvutsrqponmlkjihgfedcba.,')
     ),
    (
        ('points', 'children', 'clockwork', 'remittance', 'punctuation', 'constitution'),
        ('common', 'frequent', 'requisite', 'attractive', 'distinction', 'arrangements'),
        ('sinful', 'ambition', 'novelties', 'yardsticks', 'environment', 'approximately'),
        ('summer', 'umbrella', 'answering', 'foundation', 'explanation', 'distinguished'),
        ('behalf', 'armature', 'regarding', 'guaranteed', 'association', 'ornamentation'),
        ('exhibit', 'relieved', 'exceeding', 'sufference', 'competition', 'peculiarities'),
        ('thunder', 'citizens', 'abundance', 'atmosphere', 'transmitted', 'specification'),
        ('maximum', 'commonly', 'apparatus', 'partition', 'questionless', 'investigations'),
        ('adopting', 'pamphlets', 'accompany', 'communicate', 'installation', 'circumstances')    ),
    (
        ('123454', '098767', '123454', '098767', '123454', '098767', '123454', '098767'),
        ('123454', '098767', '123454', '098767', '123454', '098767', '123454', '098767'),
        ('123454', '098767', '123454', '098767', '123454', '098767', '123454', '098767'),
        ('123454', '098767', '123454', '098767', '123454', '098767', '123454', '098767'),
        ('123454', '098767', '123454', '098767', '123454', '098767', '123454', '098767')
    ),
    (
        ('876', '1973', '1847', '23,846', '10,746', '1,37,946'),
        ('424', '5567', '8563', '11,200', '11,140', '7,13,345'),
        ('537', '2136', '2746', '23,476', '23,450', '14,06,786'),
        ('948', '4520', '7361', '15,409', '27,763', '18,76,432'),
        ('473', '6286', '3950', '78,796', '86,521', '20,54,362'),
        ('572', '9567', '9250', '33,489', '95,362', '31,98,453')
    ),
    (
        ('July', 'Canada', 'Gandhiji', 'Minister', 'Registered'),
        ('Sita', 'Kerala', 'Varghese', 'Delivery', 'Swamimalai'),
        ('Leela', 'Bezwada', 'Strictly', 'Tamilnadu', 'Department'),
        ('March', 'Janatha', 'Govindan', 'Secretary', 'Concurrence'),
        ('Raman', 'Express', 'Exercise', 'Conferred', 'Notification'),
        ('Guntur', 'Prakash', 'Schedule', 'Government', 'Confidential'),
        ('Kannan', 'October', 'Calcutta', 'Kumbakonam', 'Superintendent')
     )    
)

PrintPara = (
    "ask fad alas asks shad lads flags flask glass\njag fag fall hash glad sags galls halls salad\njak has jags gaff hall dash flask slash flasks\nlad sad lash adds gall gash shall lakhs dhalls",

    "lad sad lash adds gall gash shall lakhs dhalls\njak has jags gaff hall dash flask slash flasks\njag fag fall hash glad sags galls halls salad\nask fad alas asks shad lads flags flask glass",

    "awerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj;\nawerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj;\nawerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj;\nawerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj;\nawerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj; awerqfa ;oiupj;",
    
    'fish  kodak ahead larks quail apples reader flukes fiddle  \ndead  rails sales agile isles should liquid shower saddle  \nidols jaded sails filed legal folder sledge squall larger  \ngrade jails lakes roses rupee squeal fields lulled dislike \napple dirks lease equip skill easels dollar poorer require \nasked forks hedge would grass jokers jailer equals refresh \nfails usual liked walks peaks orders follow drawls defiles',

    'gftfrf hjyjuj gftfrf hjyjuj gftfrf hjyjuj gftfrf hjyjuj\ngftfrf hjyjuj gftfrf hjyjuj gftfrf hjyjuj gftfrf hjyjuj\ngftfrf hjyjuj gftfrf hjyjuj gftfrf hjyjuj gftfrf hjyjuj\ngftfrf hjyjuj gftfrf hjyjuj gftfrf hjyjuj gftfrf hjyjuj\ngftfrf hjyjuj gftfrf hjyjuj gftfrf hjyjuj gftfrf hjyjuj',
    
    'lawyers streaks shipped  hillside herewith  proposals  \nshekels forward desired  loophole jugglers  strapples  \nhatless figures prepare  feathery freehold  struggles  \nthought thyself treated  assessed prepared  territory  \nquarter yodlers youthful although supplies  guileless  \nfreight further plougher shippers slightly  telegraph  \ndutiful pleased goodwill tortuous property  addressed  \nlaughed kettles whiskers thorough repeated  flashlight \npetrols regular equipped lilliput etiquette powerfully \nwithout waggish laughter kirkwall yesterday typewriter',

    'azxcvf lkmnbj azxcvf lkmnbj azxcvf lkmnbj azxcvf lkmnbj\nazxcvf lkmnbj azxcvf lkmnbj azxcvf lkmnbj azxcvf lkmnbj\nazxcvf lkmnbj azxcvf lkmnbj azxcvf lkmnbj azxcvf lkmnbj\nazxcvf lkmnbj azxcvf lkmnbj azxcvf lkmnbj azxcvf lkmnbj\nazxcvf lkmnbj azxcvf lkmnbj azxcvf lkmnbj azxcvf lkmnbj',

    'amazed  journal gambols  pickling vineyard grizzled   \nexcept  jackets fixture  austrian appeared frequent   \nlogical student spacing  movement joyfully premises   \nsixfold succeed western  examined accuracy fortress   \ndaybook lecture neither  vexation quantity executor   \nkindled general private  practice question deduction  \njingled amulets service  produces requires judicious  \njumbled arrival relative provoked starting materials  \nswivels fizzed  possible somewhat cylinder assessment \nviolets regaled becoming gracious thousand appearance',

    'abcdefghijklmnopqrstuvwxyz., zyxwvutsrqponmlkjihgfedcba., \nabcdefghijklmnopqrstuvwxyz., zyxwvutsrqponmlkjihgfedcba., \nabcdefghijklmnopqrstuvwxyz., zyxwvutsrqponmlkjihgfedcba., \nabcdefghijklmnopqrstuvwxyz., zyxwvutsrqponmlkjihgfedcba., \nabcdefghijklmnopqrstuvwxyz., zyxwvutsrqponmlkjihgfedcba.,',

    'points   children  clockwork remittance  punctuation  constitution   \ncommon   frequent  requisite attractive  distinction  arrangements   \nsinful   ambition  novelties yardsticks  environment  approximately  \nsummer   umbrella  answering foundation  explanation  distinguished  \nbehalf   armature  regarding guaranteed  association  ornamentation  \nexhibit  relieved  exceeding sufference  competition  peculiarities  \nthunder  citizens  abundance atmosphere  transmitted  specification  \nmaximum  commonly  apparatus partition   questionless investigations \nadopting pamphlets accompany communicate installation circumstances ',

    '123454 098767 123454 098767 123454 098767 123454 098767 \n123454 098767 123454 098767 123454 098767 123454 098767 \n123454 098767 123454 098767 123454 098767 123454 098767 \n123454 098767 123454 098767 123454 098767 123454 098767 \n123454 098767 123454 098767 123454 098767 123454 098767',

    '876 1973 1847 23,846 10,746 1,37,946  \n424 5567 8563 11,200 11,140 7,13,345  \n537 2136 2746 23,476 23,450 14,06,786 \n948 4520 7361 15,409 27,763 18,76,432 \n473 6286 3950 78,796 86,521 20,54,362 \n572 9567 9250 33,489 95,362 31,98,453',

    'July   Canada  Gandhiji Minister   Registered     \nSita   Kerala  Varghese Delivery   Swamimalai     \nLeela  Bezwada Strictly Tamilnadu  Department     \nMarch  Janatha Govindan Secretary  Concurrence    \nRaman  Express Exercise Conferred  Notification   \nGuntur Prakash Schedule Government Confidential   \nKannan October Calcutta Kumbakonam Superintendent'

)

#-----------------------
#tkinter start
#-----------------------
#tkinter status window
root = Tk();
root.title = "typing Status";
root.configure(bg="#2c3e50");

#labels
correct_label    = Label(root,text=" Correct         ",font="monospace 20",fg="#2ecc71",bg="#2c3e50");
wrong_label      = Label(root,text=" Wrong           ",font="monospace 20",fg="#e74c3c",bg="#2c3e50");
incomplete_label = Label(root,text=" Incomplete Type ",font="monospace 20",fg="#3498db",bg="#2c3e50");
stat_label       = Label(root,text=" Status          ",font="monospace 20",fg="#ecf0f1",bg="#2c3e50");

#grid a labels
correct_label.grid(row="0",column="0");
wrong_label.grid(row="1",column="0");
incomplete_label.grid(row="2",column="0");
stat_label.grid(row="3",column="0");

#value labels
correct_value    = Label(root,text="0 ",font="monospace 20 bold",fg="#2ecc71",bg="#2c3e50");
wrong_value      = Label(root,text="0 ",font="monospace 20 bold",fg="#e74c3c",bg="#2c3e50");
incomplete_value = Label(root,text="0 ",font="monospace 20 bold",fg="#3498db",bg="#2c3e50");
stat_value       = Label(root,text="↔ ",font="monospace 25 bold",fg="#ecf0f1",bg="#2c3e50");

#grid a labels
correct_value.grid(row="0",column="1");
wrong_value.grid(row="1",column="1");
incomplete_value.grid(row="2",column="1");
stat_value.grid(row="3",column="1");

#value change function
def editLabel(label,value):
    label.config(text=value);

def changeStat(value,color):
    stat_value.config(text=value,fg=color);
#-----------------------
#tkinter end
#-----------------------

#status variables
correctCount        = 0;
incorrectCount      = 0;
incompleteTypeCount = 0;


#MainLoop
while(True):
    #print para
    print("\n\n\ntype this paragraph\n")
    #GetPara = random.randint(0,(len(Para)-1)) 
    GetPara = 8;
    print(PrintPara[GetPara],"\n")

    #input
    typeData = []
    j = len(Para[GetPara])
        
    while(j != 0):
        temp = input()
        if(temp == ""):
            break
        
        SplitString = temp.strip().split(" ")
        typeData.append(SplitString);
        j -= 1

    #validation
    if(not typeData):
        print("empty")
    
    else:
        wronglyTypedWordsIndex = [];
        noAnotherError = True
        wrongCount = 0
        print(" ")
        for i in range(len(Para[GetPara])):
            try:
                length = len(typeData[i])
                if(len(Para[GetPara][i]) > len(typeData[i])):
                    print("\033[33mline",i+1,"are not fully typed :|\033[00m")
                    noAnotherError = False
                elif(len(Para[GetPara][i]) < len(typeData[i])):
                    print("\033[33mline",i+1,"extra typed :|\033[00m")
                    length = len(Para[GetPara][i])
                    noAnotherError = False
                for j in range(length):
                    if(Para[GetPara][i][j] != typeData[i][j]):
                        wrongCount+=1
                        wronglyTypedWordsIndex.append([i,j]);
                        
            except IndexError:
                print("\033[33mline",i+1,"not typed :|\033[00m")
                noAnotherError = False
                
        #update incomple type status
        if(noAnotherError == False):
            incompleteTypeCount += 1
            editLabel(incomplete_value,incompleteTypeCount)
            changeStat("↘ ","#e74c3c")

        #score session
        print("\n")
        if(wrongCount == 0 and noAnotherError):
            print("\033[32m"+Correct[random.randint(0,len(Correct)-1)].upper()+"\033[00m")
            correctCount += 1;
            #tkinter
            editLabel(correct_value,correctCount);
            changeStat("↗ ","#2ecc71");
            
        elif(wrongCount > 0):
            pointer = 0;
            if(wrongCount < 4 and wrongCount != 0):
                print("\033[31m"+Wrong[wrongCount-1].upper()+"\033[00m")
            else:
                print("\033[31m"+Wrong[3].upper()+"\033[00m")

            print("wrong count = ",wrongCount,"\n")
            incorrectCount += 1;
            #tkinter
            editLabel(wrong_value,incorrectCount);
            changeStat("↘ ","#e74c3c");
            
            #print para
            for i in range(len(typeData)):
                for j in range(len(typeData[i])):
                    if(pointer < len(wronglyTypedWordsIndex) and wronglyTypedWordsIndex[pointer][0] == i and wronglyTypedWordsIndex[pointer][1] == j):
                        print("\033[2m\033[31m"+typeData[i][j]+"\033[00m", end=" ")
                        pointer += 1;
                    else:
                        print(typeData[i][j],end=" ")
                print("")
        
        elif(noAnotherError == False):
            incorrectCount += 1
            editLabel(wrong_value,incorrectCount)

    #loop end condition
    temp2 = input("\n\nyou will continue? (press enter to continue) ")
    if(temp2 == ""):
        continue
    else:
        root.destroy();
        break
root.mainloop();

