file = input("File name: ").lower().strip().split(".")
app = ['pdf','zip']
img = ['jpg','jpeg']
p = ['png','gif']


if file[-1] =='txt':
    print('text/plain')
elif file[-1] in img:
    print(f'image/jpeg')
elif file[-1] in p:
    print(f'image/{file[-1]}')
elif file[-1] in app:
    print(f'application/{file[-1]}')
else:
    print('application/octet-stream')
