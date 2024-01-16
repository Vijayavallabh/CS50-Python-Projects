import random
while True:
    text = input('Level :')
    if text.isnumeric():
        try:
            text = int(text)
            b = int(input('Guess: '))
            a= random.randint(1,text)
            if a == b:
                print('Just right!')
                break
            elif a<b:
                print('Too large!')
                pass
            elif a>b:
                print('Too small!')
                pass
        except:
            pass


    else:
        pass
