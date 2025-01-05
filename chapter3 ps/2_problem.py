from datetime import datetime
name = input('What is your name: ')
date = str(datetime.now().date())
letter = '''Dear <|Name|>,
Yor are so good.
<|Date|>'''
print(letter.replace('<|Name|>',name).replace('<|Date|>',date))