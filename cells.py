from tkinter import  Button
import random
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

    def right_click_actions(self, event):
        print(event)
        print("right Clicked!!")