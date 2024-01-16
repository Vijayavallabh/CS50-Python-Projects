am = 50
while am>=0:
    print('Amount Due:',am)
    l = ['10','25','5']
    text = input('Insert Coin: ')
    if text in l:
        am = am - int(text)
        if am == 0:
           print('Change Owed:',am)
           break
        if am<0:
            print('Change Owed:',-am)


