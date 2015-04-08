import re
fileopen = open('Apple.txt')
s =str()
while True:             
    line = fileopen.readline()  #讀寫一行
    s = s + line
    if len(line) ==0:           #檢視是否有字串
        break
   
    #print (line)
fileopen.close()

#print(s)




def list2freqdict(mylist):
    mydict=dict()
    for ch in mylist:
        mydict[ch]=mydict.get(ch,0)+1
    return mydict

t = re.findall("[\w]+",s)
#print(t)
chfreqdict=list2freqdict(t)
#print(chfreqdict)

from operator import itemgetter
chfreqsorted=sorted(chfreqdict.items(), key=itemgetter(1), reverse=True)

def list2bigram(mylist):
    return [mylist[i:i+2] for i in range(0,len(mylist)-1)]


chbigram=list2bigram(t)
def bigram2freqdict(mybigram):
    mydict=dict()
    for (ch1,ch2) in mybigram:
        mydict[(ch1,ch2)]=mydict.get((ch1,ch2),0)+1
    return mydict

bigramfreqdict=bigram2freqdict(chbigram)
bigramfreqsorted=sorted(bigramfreqdict.items(), key=itemgetter(1), reverse=True)
five = bigramfreqsorted[:5]
def freq2report(freqlist):
    chs=str()
    print('Char(s)\tCount')
    print('=============')
    for (token,num) in freqlist:
        for ch in token:
            chs=chs+" "+ch
        print(chs,'\t',num)
        chs=''
    return

freq2report(five)
freq2report(bigramfreqsorted)
