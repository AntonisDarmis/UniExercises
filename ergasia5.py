with open('demofile.txt','r') as f:
    Words=[word for line in f for word in line.split()]

#Removing Special characters,dots and numbers    
for idx, word in enumerate(Words):
    temp=Words[idx]
    Words[idx]=''.join(l for l in temp if l.isalnum())
    if Words[idx].isnumeric()== True:
        Words.remove(Words[idx])
    temp=temp.replace('.','')
    temp=temp.replace(',','')
      
        
for idx, word in enumerate(Words):
    temp=Words[idx]
    if len(temp)>3:
        print("Word is:",temp)
        temp=list(temp)
        first=temp[0]
        temp.remove(temp[0])
        temp.append(first)
        temp.append("ay")
        temp=''.join(temp)
        print("Word after removing first letter and concatenating it with 'ay' is:",temp) 
        
