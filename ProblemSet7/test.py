import string
def isWordIn(word,text):
    exclude = set(string.punctuation)
    temp = ''
    for ch in text:
        if ch not in exclude:
            temp += ch
        else:
            temp += ' '
    temp = temp.split(' ')
    temp = [item.lower() for item in temp]
    temp2 = word.lower()
    #print temp
    #print temp2
    return temp2 in temp
    
print isWordIn('soft','Koala bears are soft and cuddly.')
print isWordIn('soft','I prefer pillows that are soft.')
print isWordIn('soft','Soft drinks are great.')
print isWordIn('soft',"Soft's the new pink!")
print isWordIn('soft','"Soft!" he exclaimed as he threw the football.')
print isWordIn('soft','Microsoft recently released the Windows 8 Consumer Preview.')
print isWordIn('soft','Downey makes my clothes the softest they can be!')