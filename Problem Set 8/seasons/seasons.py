from datetime import date
import inflect
import operator
import sys
p=inflect.engine()
def main():
    try:
        a = input('Date of Birth: ')
        b = operator.sub(date.today(), date.fromisoformat(a))
        print(convert(b.days))
    except ValueError:
        sys.exit('Invalid Date')
def convert(t):
    s = t*24*60
    return f"{(p.number_to_words(s, andword='')).capitalize()} minutes"


if __name__ == "__main__":
    main()
