import validators
if email_add := validators.email(input("What's your email address: ")):
    print('Valid')
else:
    print('Invalid')

