text = input("Greetings: ").lower().strip()
if text.startswith('hello'):
    print('$0')
elif text.startswith('h'):
    print('$20')
else:
    print('$100')
