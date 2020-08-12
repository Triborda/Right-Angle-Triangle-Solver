#########################
# import needed modules #
#########################
import tkinter
from tkinter import Tk, Canvas, Frame, BOTH


#########################
# create triangle class #
#########################
class Triangle(Frame):
    def __init__(self):
        # call the init of Frame
        super().__init__()
        self.init_ui()

    # define ui for triangle
    def init_ui(self):
        # set title of window
        self.master.title("Right Angle Triangle Calculator")
        # allow the triangle to fill the screen
        self.pack(fill=BOTH, expand=1)
        # set the canvas
        canvas = Canvas(self)
        # set up the points that make the triangle
        triangle_1 = (125, 75)
        triangle_2 = (125, 215)
        triangle_3 = (265, 215)
        square_1 = (125, 205)
        square_2 = (135, 205)
        square_3 = (135, 215)
        x = (0)
        y = (0)
        # set triangle in frame
        canvas.create_line(triangle_1, triangle_2, triangle_3, triangle_1)
        # set square in frame
        canvas.create_line(square_1, square_2, square_3)
        # set point a in frame
        canvas.create_text(100, 150, anchor="w", font="Arial", text="a")
        # set point A in frame
        canvas.create_text(275, 235, anchor="w", font="Arial", text="A")
        # set point b in frame
        canvas.create_text(185, 235, anchor="w", font="Arial", text="b")
        # set point B in frame
        canvas.create_text(100, 50, anchor="w", font="Arial", text="B")
        # set point c in frame
        canvas.create_text(205, 130, anchor="w", font="Arial", text="c")
        # set point C in frame
        canvas.create_text(100, 235, anchor="w", font="Arial", text="C")

        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Triangle()
    # set position on screen
    root.geometry("400x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
