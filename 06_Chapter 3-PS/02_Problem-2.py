#Write a program to fill in a letter template given below with name and date
letter ='''Dear <|Name|,
You are selected!
<|Date|>
        '''
print(letter.replace("<|Name|","Awais").replace("<|Date|>", "18 August 2027"))