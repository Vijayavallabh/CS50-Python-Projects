import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if b := re.findall(r'(^|\W)um($|\W)',s,re.IGNORECASE):
        return len(b)


if __name__ == "__main__":
    main()
