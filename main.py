from tkinter import *
from json import *
root = Tk()
root.geometry('800x1000')

def bookseat(event):
    if event.widget.free:
        event.widget.config(bg='red')
        Label(root, text=f'{event.widget.row} {event.widget.place} is booked').place(x=10, y=850)

def hasher(row, place):
    return 100*row+place

def freeseats():
    # for i in range(len(seats)):
    #     for j in range(len(seats[i])):
            seats[hasher(i, j)] = True
            if not seats[i][j].free:
                with open(freeseats.json, 'w') as file:
                    dump(seats, file)


seats = {}
seats = [[Button(root, text=i, width =4, height =2, bg = 'green') for i in range (1, 16)] for g in range(20)]
for i in range(len(seats)):
    for j in range(len(seats[i])):
        seats[i][j].free = True
        seats[i][j].price = 3000-100*i
        seats[i][j].row = i+1
        seats[i][j].place = j+1
        seats[i][j].grid(row=i, column=j)
        seats[i][j].bind('<Button-1>', bookseat)
for i in range(len(seats)):
    Label(root, text=i+1).grid(row=i, column=16)
    Label(root, text=3000-100*i).grid(row=i, column=17)

places = {}
for i in range(len(seats)):
    for j in range(len(seats[i])):
        places[hasher(i, j)] = True
with open('seats.json', 'w') as file:
    dump(places, file)

root.mainloop()