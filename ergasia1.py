#Opening and reading given file.
with open('demofile.txt','r') as f:
    BiggestWords=[word for line in f for word in line.split()]
print(BiggestWords)

for idx, word in enumerate(BiggestWords):
    temp=BiggestWords[idx]
    BiggestWords[idx]=''.join(l for l in temp if l.isalnum())
    if BiggestWords[idx].isnumeric()== True:
        BiggestWords.remove(BiggestWords[idx])
    temp=temp.replace('.','')
    temp=temp.replace(',','')
    
#Descending list with all the words and removing duplicates
BiggestWords = list(dict.fromkeys(BiggestWords))
BiggestWords.sort(key=len)
BiggestWords.reverse()
print(BiggestWords)
for i in range(5):
    #Splitting the 5 biggest words into letters
    temp=BiggestWords[i]
    print('Word is',temp)
    for x in temp:
        #Detecting vowel,removing it,reversing word's character list and joining the characters
        if x in "aeiou":
            temp = temp.replace(x," ")
    #Removing spaces,joining the separate characters and reversing the word
    #temp = " ".join(temp.split())
    temp = temp.replace(" ", "")
    temp = temp[::-1]
    print('Final is',temp)

            
            
