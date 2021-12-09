# from _typeshed import Self
from tkinter import  Button
import random
from tkinter.constants import S
import settings

class Cell:
    all =[]
    def __init__(self, x, y, is_mine = False) -> None:
        self.is_mine = is_mine
        self.x = x
        self.y = y
        self.cell_btn_object = None

        Cell.all.append(self)
    


    def create_btn_object(self, location):
        btn = Button(location,width=12, height=4, text=f"{self.x},{self.y}")

        btn.bind('<Button-1>', self.left_click_actions ) # Left Click
        btn.bind('<Button-3>', self.right_click_actions ) # Right Click

        self.cell_btn_object = btn

    
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)

        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    
    def __repr__(self) -> str:
        return f"Cell({self.x},{self.y})"






    def left_click_actions(self, event):
        print(event)
        print("Left Clicked!!")
        if self.is_mine:
            self.cell_btn_object.configure(bg='red')
        else:
            self.show_cell()

    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y -1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]

        cells = [cell for cell in cells if cell is not None]

        return cells
    @property
    def get_surrounding_mines(self):
        counter = 0

        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter


    def show_cell(self):
        self.cell_btn_object.configure(text=self.get_surrounding_mines)



    def right_click_actions(self, event):
        print(event)
        print("right Clicked!!")