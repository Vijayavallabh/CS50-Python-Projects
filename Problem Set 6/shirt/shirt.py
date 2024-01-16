from sys import argv, exit
import os
from PIL import ImageOps as i, Image as j
if len(argv) != 3:
    if len(argv) < 3:
        exit('Too few command-line arguments')
    else:
        exit('Too mant command-line arguments')
fi,fo = argv[1],argv[2]
in_root, in_ext = os.path.splitext(fi)
out_root, out_ext = os.path.splitext(fo)
if in_ext.lower() != out_ext.lower():
    exit('Input and output have different extensions')
if in_ext.lower() == '.jpg' or in_ext.lower() == '.jpeg' or in_ext.lower() == '.png':
    pass
else:
    exit('Invalid input')
if out_ext.lower() == '.jpg' or out_ext.lower() == '.jpeg' or out_ext.lower() == '.png':
    pass
else:
    exit('Invalid output')
try:
    shirt = j.open('shirt.png')
    muppet = j.open(fi)
except FileNotFoundError:
    exit('Input does not exist')
except Exception as exp:
    exit(exp)
size = shirt.size
b = i.fit(muppet, size)
b.paste(shirt, shirt)
b.save(fo)

