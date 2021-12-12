# from _typeshed import Self
from tkinter import  Button, Label
import random
from tkinter.constants import S
import settings
import ctypes
import sys

class Cell:
    all =[]
    cell_count = settings.CELL_COUNT
    cell_count_label_obj = None
    def __init__(self, x, y, is_mine = False) -> None:
        self.is_mine = is_mine
        self.x = x
        self.y = y
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None

        Cell.all.append(self)
    


    def create_btn_object(self, location):
        btn = Button(location,width=12, height=4, text=f"{self.x},{self.y}")

        btn.bind('<Button-1>', self.left_click_actions ) # Left Click
        btn.bind('<Button-3>', self.right_click_actions ) # Right Click

        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left:{Cell.cell_count}",
            font=("", 30)
        )

        Cell.cell_count_label_obj = lbl



    
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
            ctypes.windll.user32.MessageBoxW(0,'You clicked on a mine', 'Game Over', 0)
            sys.exit()
        else:
            self.show_cell()
            if self.get_surrounding_mines == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            
            # If mines count is equal to cells left count, then the player won the game
            if settings.MINES_COUNT == Cell.cell_count:            
                ctypes.windll.user32.MessageBoxW(0,'YOU WON THE GAME', 'Game Over', 0)


        # Cancel left and right click events if button is already opened/ already clicked
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

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

        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.get_surrounding_mines)

            if Cell.cell_count_label_obj:
                Cell.cell_count_label_obj.configure(
                    text=f"Cells Left:{Cell.cell_count}"
                )
            
            if self.is_mine_candidate:
                self.cell_btn_object.configure(bg='SystemButtonFace')
        
        self.is_opened = True



    def right_click_actions(self, event):
        print(event)
        print("right Clicked!!")
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg='orange')
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(bg='SystemButtonFace')
            self.is_mine_candidate = False