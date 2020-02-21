with open('demofile.txt','r') as f:
    Text=[word for line in f for word in line.split()]
print (Text)
#Removing Special characters,dots and numbers
for idx, word in enumerate(Text):
    temp=Text[idx]
    Text[idx]=''.join(l for l in temp if l.isalnum())
    if Text[idx].isnumeric()== True:
        Text.remove(Text[idx])
    temp=temp.replace('.','')
print(Text)   
for idx, word in enumerate(Text):
    temp=Text[idx]
    print ("The word is:",temp)
    temp=list(temp)
    consonant=0
    for x in temp:
        if x in "fckr":
            consonant=consonant+1
    length=len(temp)
    spare=length-consonant
    if consonant>spare:
        print("Bad word")
    else:
        print("Good word")
        
        
    
         
        
         
         
    
    
    
