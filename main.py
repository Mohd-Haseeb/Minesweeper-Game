from tkinter import *
from cells import Cell
import settings
import utils

root = Tk()


# Overriding the settings of the window
root.configure(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.resizable(False,False)
root.title("Mine Sweeper Game")


# top frame
top_frame = Frame(
    root,
    bg='red',
    width=settings.WIDTH,
    height=utils.height_prcnt(25),
)

top_frame.place(x=0,y=0)


# left frame
left_frame = Frame(
    root,
    bg='blue',
    width=utils.widtht_prcnt(25),
    height=utils.height_prcnt(75),
)

left_frame.place(x=0,y=utils.height_prcnt(25))


# main frame or center frame
center_frame = Frame(
    root,
    bg='green',
    width=utils.widtht_prcnt(75),
    height=utils.height_prcnt(75),
)

center_frame.place(x=utils.widtht_prcnt(25),y=utils.height_prcnt(25))


# btn = Button(center_frame, text = 'click')
# btn.place(x=0,y=0)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell()
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x, row=y)


# run the window
root.mainloop()