text = input('camelCase: ')
for i in text:
    if i.isupper()==True:
        i= '_'+i.lower()
    print(i,end = '')
print('\n')

