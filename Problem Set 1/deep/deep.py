text = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
l = ["42", "forty two", "forty-two"]
if  text in l:
    print('Yes')
else:
   print('No')
