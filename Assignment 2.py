import numpy as np
import string
key= input('What is your key:\n')
text= input('What is the text:\n')
function= input('What do you want to do encrypt or decypt:\n')
key=key.lower()
text=text.lower()
function= function.lower()
alphabets= string.ascii_lowercase
list=[]
word=[]
updated_word=''

#iteration to come up with a list from your key
for letter in key:
    if letter in alphabets:
        if letter in list:
            pass
        elif letter == 'i':
            if 'j' in list:
                pass
            else:
                list.append(letter)
        elif letter == 'j':
            if 'i' in list:
                pass
        else:
            list.append(letter)
#here we come up with the 5 by 5 arraay
for letter in alphabets:
    if letter in list:
            pass
    elif letter == 'i':
        if 'j' in list:
            pass
        else:
            list.append(letter)
    elif letter == 'j':
        if 'i' in list:
            pass
        else:
            list.append(letter)
    else:
        list.append(letter)
l= np.array(list)
a= l.reshape((5,-1))#5 by 5 array

#function to seperate string into pairs
def sep(inp):
    if len(inp)%2!=0:
        inp+='x'
    for i in range(0,len(inp),2):
        if word==[]:
            message=inp[0]+inp[1]
            word.append(message)
        else:
            news= inp[i:i+2]
            word.append(news)
sep(text)

#iteration to adjust like characters
for s in word:
    if len(s)>1:
        if s[0] == s[1]:
            updated_word+= s[0]+'x'+s[1]
        elif s[1]=='x':
            updated_word+=s[0]
        else:
            updated_word+=s[0]+s[1]
word=[]
sep(updated_word)

#function to code the input
def playfair_cipher(word,function):
    if function=='encrypt':
        code=''
        #a is the 5by5 array dine with numpy
        for pair in word:
            if pair[0] =='i' and 'i' not in a:
                pair[0]='j'
            if pair[1] =='i' and 'i' not in a:
                pair[1]='j'
            if pair[0] =='j' and 'i' not in a:
                pair[0]='i'
            if pair[1] =='j' and 'i' not in a:
                pair[1]='i'          
            first = np.where(a==pair[0])
            second= np.where(a==pair[1])
            if first[0]==second[0]:
                new_p= (first[1][0]+1)%5
                new_p2= (second[1][0]+1)%5
                code+= a[first[0][0]][new_p]+a[second[0][0]][new_p2]
            elif first[1]==second[1]:
                new_p= (first[0][0]+1)%5
                new_p2= (second[0][0]+1)%5
                code+= a[new_p][first[1][0]]+a[new_p2][second[1][0]]
            else:
                code+=a[first[0][0]][second[1][0]]+ a[second[0][0]][first[1][0]]
        return code
    if function=='decrypt':
        code=''
        for pair in word:
            if pair[0] =='i' and 'i' not in a:
                pair[0]='j'
            if pair[1] =='i' and 'i' not in a:
                pair[1]='j'
            if pair[0] =='j' and 'i' not in a:
                pair[0]='i'
            if pair[1] =='j' and 'i' not in a:
                pair[1]='i'  
            first = np.where(a==pair[0])
            second= np.where(a==pair[1])
            if first[0]==second[0]:
                new_p= (first[1][0]-1)%5
                new_p2= (second[1][0]-1)%5
                code+= a[first[0][0]][new_p]+a[second[0][0]][new_p2]
            elif first[1]==second[1]:
                new_p= (first[0][0]-1)%5
                new_p2= (second[0][0]-1)%5
                code+= a[new_p][first[1][0]]+a[new_p2][second[1][0]]
            else:
                code+=a[first[0][0]][second[1][0]]+ a[second[0][0]][first[1][0]]
        for i in range(len(code)-3,2):#removing the x's
            if code[i]== code[i+2]:
                if code[i+1]=='x':
                    code=code.replace(code[i+1],'')
        if code[-1]=='x':
            code= code.replace(code[-1],'')

        return code
print(playfair_cipher(word,function))
