from tkinter import *
from json import dump, load
from datetime import datetime
import requests

def start_seats():
    '''
    Creating a new file of available seats, if such file doesn't exist.
    '''
    # Hashing every seat with code with number of row and column
    places = {}
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            places[hasher(i, j)] = True
    with open('seats.json', 'w') as file:
        dump(places, file)


def read_seats():
    with open("seats.json", "r") as file:
        return load(file)

def write_seats(places):
    with open('seats.json', 'w') as file:
        dump(places, file)


def bookseat(event):
    '''
    Making every free seat booked. Controls every button by means of event.
    If current seat is free, makes it red and booked.
    Shows label about current booked seat.
    :param event:
    :return:
    '''
    if event.widget.free:
        event.widget.config(bg='red')
        Label(root, text=f'{event.widget.row} {event.widget.place} is booked').place(x=10, y=850)
        places[hasher(event.widget.row - 1, event.widget.place - 1)] = False
        write_seats(places)
        person = pstr.get()
        if person == "":
            person = "Anonymous"
        write_seats(places)
        write_log(create_log(event.widget.row, event.widget.place, event.widget.price, person))


def hasher(row, place):
    '''
    Creating unique code for every seat
    :param row: row
    :param place: column
    :return: code as integer
    '''
    return str(100 * row + place)


def create_log(row, place, price, person):
    '''
    Creating a string for log file
    :param person: nickname of user
    :param row: row
    :param place: place
    :param price: price of place
    :return: formatted string for log file
    '''
    return f"{datetime.now()} <<{person}>> row: {row} place: {place} -> {price}"


def write_log(text, filename="log.txt"):
    with open(filename, "a") as file:
        file.writelines([text + '\n'])

def currency_converter(rb, money):
    # money = rb.get()
    money = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()["Valute"]

    if rb == rb2:
        seatslabel.config(root, text=f"{3000 - 100 * i // money['USD']['Valute']} USD", font='Arial').grid(row=i, column=17)
    elif rb == rb3:
        seatslabel.config(root, text=f"{3000 - 100 * i // money ['EUR']['Valute']} EUR", font='Arial').grid(row=i, column=17)
    elif rb == rb4:
        seatslabel.config(root, text=f"{3000 - 100 * i // money['JPY']['Valute']} JPY", font='Arial').grid(row=i, column=17)
    elif rb == rb5:
        seatslabel.config(root, text=f"{3000 - 100 * i // money['AUD']['Valute']} AUD", font='Arial').grid(row=i, column=17)
    else:
        seatslabel.config(root, text=f"{3000 - 100 * i // money['CAD']['Valute']} CAD", font='Arial').grid(row=i, column=17)


# Creating main window
root = Tk()
root.geometry('1000x1000')
# Creating matrix of seats
seats = [[Button(root, text=i, width=4, height=2) for i in range(1, 16)] for g in range(20)]
# Try to load info about current seats
try:
    places = read_seats()
except FileNotFoundError:
    start_seats()
    places = read_seats()
except:
    print("Something is going wrong!")
# Printing matrix of seats to the window
for i in range(len(seats)):
    for j in range(len(seats[i])):
        seats[i][j].free = places[hasher(i, j)]
        seats[i][j].price = 3000 - 100 * i
        seats[i][j].row = i + 1
        seats[i][j].place = j + 1
        seats[i][j].grid(row=i, column=j)
        seats[i][j].bind('<Button-1>', bookseat)
        if seats[i][j].free:
            seats[i][j].config(bg=f"#00{hex(255 - 10 * i)[2:]}00", fg=("black" if i < 10 else "white"))
        else:
            seats[i][j].config(bg="red")
# Printing prices of all rows
for i in range(len(seats)):
    Label(root, text=i + 1).grid(row=i, column=16)
    seatslabel = Label(root, text=f"{3000 - 100 * i} RUB", font='Arial').grid(row=i, column=17)

rb = IntVar()
rb1 = Radiobutton(text='Ruble', font='Arial', value=0, variable=rb).place(x=700, y=70)
rb2 = Radiobutton(text='USD', font='Arial', value=1,variable=rb).place(x=700, y=140)
rb3 = Radiobutton(text='Euro', font='Arial',value=2,variable=rb).place(x=700, y=210)
rb4 = Radiobutton(text='The Japanese Yen', font='Arial',value=3, variable=rb).place(x=700, y=280)
rb5 = Radiobutton(text='The Australian Dollar', font='Arial',value=4,variable=rb).place(x=700, y=350)
rb6 = Radiobutton(text='The Canadian Dollar', font='Arial',value=5,variable=rb).place(x=700, y=410)

try:
    places = read_seats()
except FileNotFoundError:
    start_seats()
    places=read_seats()
except:
    print("Something is going wrong!")

pstr = StringVar()
nameLabel = Label(root, text='Enter your name: ', font='Arial').place(x=250, y=820)
nameField = Entry(root, textvariable=pstr).place(x=250, y=850)

try:
    money = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()["Valute"]
except:
    print("Problems with internet connection!")
else:
    print(money["AUD"]["Value"])

root.mainloop()


