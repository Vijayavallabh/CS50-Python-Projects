def main():
    text= input('Greeting: ')
    fine = value(text)
    print('$'+str(fine))

def value(t):

    t = t.lower().strip()

    if 'hello' in t:
        return(0)
    elif 'h' in t[0]:
        return(20)
    else:
        return(100)


if __name__ == "__main__":
    main()
