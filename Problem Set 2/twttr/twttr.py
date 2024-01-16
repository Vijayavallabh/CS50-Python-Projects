text = input('Input: ')
for i in text:
    if i.lower() not in ['a','e','i','o','u']:
        print(i,end = '')
