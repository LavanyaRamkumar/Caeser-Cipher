import string

def checkWord(l,wordList):
        c=0
        for i in l:
                if(i in wordList):
                        c+=1
        return (c==len(l))        
        return 1

def decryption(st,wordList):
        for i in range(1,26):
                l=[]
                s=[]
                for j in range(len(st)):
                        asc = ord(st[j])+i 
                        if(ord(st[j]) == 32):
                                l.append("".join(s))
                                s=[]
                        elif (asc > 122): 
                                s+=chr(ord(st[j])+i-26)
                        else:
                                s+=chr(ord(st[j])+i)
                        if(j==len(st)-1):
                                l.append("".join(s))
                if(checkWord(l,wordList) == 1):
                        print(" ".join(l) )
                        if(i>13):
                                print("Key:",i-26)
                        else:
                                print("Key:",i)

def loadWords(WORDLIST_FILENAME):
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print (len(wordList), "words loaded")
    return wordList

def main():
        wordList=[]
        WORDLIST_FILENAME = "words.txt"
        wordList = loadWords(WORDLIST_FILENAME)
        print()
        t=int(input("Number of test cases"))
        for i in range(t):
                print()
                st=input()
                decryption(st,wordList)

if __name__ == "__main__":
        main()
        

