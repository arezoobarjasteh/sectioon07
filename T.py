try:
    read_dict=open('words.txt', 'r')
    mywords = read_dict.read()
    words=[]  
    wordslist=mywords.split('\n')
    for i in range (0,len(wordslist),2):
        words.append({"english":wordslist[i], "persian":wordslist[i+1]})   
    read_dict.close()      
except:
    print('peida nashod , didnt found')
def translatetoenglish():
    sentence = input('vared farmaid')
    persianword = sentence.split(' ')
    for i in range(len(persianword)):
        for j in range(len(words)):
            if words[j]['persian'] ==persianword[i]:
                print(words[j]['english'], end=' ')
                break
        else:
            print(persianword[i], end=' ')
def translatetopersian():
    sentence =input("Enter your sentence : ")
    enwords= sentence.split(' ')
    for i in range(len(enwords)):
        for j in range(len(words)):
            if words[j]['english'] ==enwords[i]:
                print(words[j]['persian'], end=' ')
                break
        else:
            print(enwords[i], end=' ')         
def AddNewWord():
    English=input("kalame ra vared farmaid baray ezafe kardan ")
    Persian=input("maenish?")
    words.append({'english': English,'persian': Persian})
    print('anjam shod')
    open_dict = open('words.txt', 'a')
    open_dict.write('\n'+English)
    open_dict.write('\n'+Persian)
    open_dict.close()
while True:
    print("1-ezafe kardan 2-englisi be farsi 3- farsi be englisi 4- khoroj")
    choice =input("entekhab konid ") 
    if choice=='1':
        AddNewWord()
    elif choice=='2':
        translatetopersian()
    elif choice=='3':
        translatetoenglish()
    elif choice=='4':
        exit