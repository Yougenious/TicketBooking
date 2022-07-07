from tkinter import *
from json import *


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


def hasher(row, place):
    '''
    Creating unique code for every seat
    :param row: row
    :param place: column
    :return: code as integer
    '''
    return 100 * row + place



# Creating main window
root = Tk()
root.geometry('800x1000')
# Creating matrix of seats
seats = [[Button(root, text=i, width=4, height=2, bg='green') for i in range(1, 16)] for g in range(20)]
# Printing matrix of seats to the window
for i in range(len(seats)):
    for j in range(len(seats[i])):
        seats[i][j].free = True
        seats[i][j].price = 3000 - 100 * i
        seats[i][j].row = i + 1
        seats[i][j].place = j + 1
        seats[i][j].grid(row=i, column=j)
        seats[i][j].bind('<Button-1>', bookseat)
# Printing prices of all rows
for i in range(len(seats)):
    Label(root, text=i + 1).grid(row=i, column=16)
    Label(root, text=3000 - 100 * i).grid(row=i, column=17)

try:
    places = read_seats()
except FileNotFoundError:
    start_seats()
    places=read_seats()
except:
    print("Something is going wrong!")

print(read_seats())

root.mainloop()
