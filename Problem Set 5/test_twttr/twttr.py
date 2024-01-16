def main():
    inpt= input('Input: ')
    a = shorten(inpt)
    print('Output:', a)

def shorten(word):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for i in vowels:
        if i in word:
            word = word.replace(i, '')
    return word
if __name__ == "__main__":
    main()
