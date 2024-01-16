while True:
   try:
      text1,text3 = input('Fraction: ').split('/')
      if int(text1)<=int(text3)and int(text3)!=0:
         text = int(round(int(text1)/int(text3)*100,0))
         if 100>=text>=99:
            print("F")
            break
         elif 0<=text<=1:
            print("E")
            break
         else:
            print(f'{text}%',end = '')
            break
   except (ValueError,ZeroDivisionError):
      pass

