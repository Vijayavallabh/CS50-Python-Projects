def main():
    text = input("What time is it? ")
    if 7.00 <=convert(text)<=8.00:
        print('Breakfast time')
    elif 12.00<=convert(text)<=13.00:
        print('Lunch time')
    elif 18.00<=convert(text)<=19.00:
        print('Dinner Time')
    else:
        return


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)/60
    return hours+minutes

if __name__ == "__main__":
    main()
