def main():
    text = input('Enter a text with emoji: ')
    print(convert(text))

def convert(text):
    text1 = text.replace(":)", '🙂').replace(":(",'🙁')
    return text1


main()
