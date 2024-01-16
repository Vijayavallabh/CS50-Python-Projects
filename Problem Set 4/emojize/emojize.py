import emoji
from emoji import emojize

text = input("Input: ")
output = emoji.emojize(text,language = 'alias')

print("Output:", output)
