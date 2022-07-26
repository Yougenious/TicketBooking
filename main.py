from tkinter import *
from json import *
from datetime import *
import random

def start_seats():
    '''
    Creating a new file of available seats, if such file doesn't exist.
    '''
    # Hashing every seat with code with number of row and column
    places = {}
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            places[hasher(i, j)] = Truefrom tkinter import *
from json import dump, load
from datetime import datetime
# import requests

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

def pricing():
    for i in range(len(seats)):
        Label(root, text=i + 1).grid(row=i, column=16)
        Label(root, text=f"{3000 - 100 * i} RUB", font='Arial').grid(row=i, column=17)

def currency_converter(row, currency, money, dollar, euro, yen, ausdol, candol):
    currency = rb.get()
    money = {dollar, euro, yen, ausdol, candol}
    money = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()["Valute"]
    money1 = pricing
    #dollar = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()["USD"].rb.get()
    #euro = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()["EUR"].rb.get()
    #yen = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()["JPY"].reb.get()
    #ausdol = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()["AUD"].rb.get()
    #candol = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()["CAD"].rb.get()

    amount = row.get()

    if currency == dollar:
        pricing.config(text= amount * dollar)
    elif currency == euro:
        pricing.config(text= amount * euro)
    elif currency == yen:
        pricing.config(text= amount * yen)
    elif currency == ausdol:
        pricing.config(text= amount * ausdol)
    else:
        pricing.config(text= amount * candol)


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
    Label(root, text=f"{3000 - 100 * i} RUB", font='Arial').grid(row=i, column=17)

rb = DoubleVar()
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


def hasher(row, place):
    '''
    Creating unique code for every seat
    :param row: row
    :param place: column
    :return: code as integer
    '''
    return str(100 * row + place)


def create_log(person, data, row, place, price):
    '''
    Creating a string for log file
    :param person: nickname of user
    :param data: data of booking
    :param row: row
    :param place: place
    :param price: price of place
    :return: formatted string for log file
    '''
    return f"{data} <<{person}>> row: {row} place: {place} -> {price}"


def write_log(text, filename):
    #TODO: write a function which writes string_log to log file
    with open(filename, "a") as file:
        file.writelines([text + '\n'])

def colour_seats():
    places={}
    for i in range(3):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb = [r, g, b]
    #hexcolour = hex(rgb)
    # i = 0
    # i += 1 = hexcolour += 12
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j].free:
                seats[i][j].config(bg='rgb')
            else:
                seats[i][j].config(bg="red")

# Creating main window
root = Tk()
root.geometry('800x1000')
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
            seats[i][j].config(bg="green")
        else:
            seats[i][j].config(bg="red")
# Printing prices of all rows
for i in range(len(seats)):
    Label(root, text=i + 1).grid(row=i, column=16)
    Label(root, text=3000 - 100 * i).grid(row=i, column=17)


root.mainloop()
