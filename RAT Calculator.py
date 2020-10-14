#########################
# import needed modules #
#########################
from tkinter import *
import math
import time


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
    # keep window running
    root.mainloop()


# open right angle triangle window
if __name__ == '__main__':
    main()

####################
# preset variables #
####################
# used in a function to stop overlap of labels
done = False
# define values
values = False
# keep values loop running
x = True

#####################
# add to GUI window #
#####################
# create window
window = Tk()
# title window
window.title("Right Angle Triangle Calculator")


#####################################
# input value for angle A functions #
#####################################
# function for when degrees option selected
def degrees():
    # allow other functions to access angle_type
    global angle_type
    # allow the button to be pressed
    done_button.configure(text="Input value", state="normal")
    # set the angle type to degrees
    angle_type = "deg"


# function for when radians function selected
def radians():
    # allow other functions to access angle_type
    global angle_type
    # allow button to be pressed
    done_button.configure(text="Input value", state="normal")
    # set the angle type to radians
    angle_type = "rad"


# function for setting input values to variables
def get_values():
    global angle_type, a_angle_input, done, values
    # preset values state
    values = False
    # get needed variables from the global

    if a_angle_input.get() != "" and isinstance(a_angle_input.get(), str):
        # if the angles are in degrees
        if angle_type == "deg":
            # get the value and convert to integer then radians
            a_rad = math.radians(float(a_angle_input.get()))
            # get the value and convert to integer
            a_deg = float(a_angle_input.get())
        # else if the angle type is in radians
        elif angle_type == "rad":
            # set the angle to the value in radians
            a_rad = float(a_angle_input.get())
            # set the angle to the value in degrees
            a_deg = math.degrees(float(a_angle_input.get()))
        # variable to make deciding on SOH CAH TOA easier
        a_angle_use = True
    else:
        a_angle_use = False
        a_rad = ""

    if b_angle_input.get() != "" and isinstance(b_angle_input.get(), str):
        # if the angles are in degrees
        if angle_type == "deg":
            # get the value and convert to integer then radians
            b_rad = math.radians(float(b_angle_input.get()))
            # get the value and convert to integer
            b_deg = float(b_angle_input.get())
        # else if the angle type is in radians
        elif angle_type == "rad":
            # set the angle to the value in radians
            b_rad = float(b_angle_input.get())
            # set the angle to the value in degrees
            b_deg = math.degrees(float(b_angle_input.get()))
        # variable to make deciding on SOH CAH TOA easier
        b_angle_use = True
    else:
        b_angle_use = False
        b_rad = ""

    if a_side_input.get() != "":
        a_side = float(a_side_input.get())
        # variable to make deciding on SOH CAH TOA easier
        a_side_use = True
    else:
        a_side_use = False
        a_side = ""

    if b_side_input.get() != "":
        b_side = float(b_side_input.get())
        # variable to make deciding on SOH CAH TOA easier
        b_side_use = True
    else:
        b_side_use = False
        b_side = ""

    if c_side_input.get() != "" and isinstance(c_side_input.get(), str):
        c_side = float(c_side_input.get())
        # variable to make deciding on SOH CAH TOA easier
        c_side_use = True
    else:
        c_side_use = False
        c_side = ""
    if a_angle_use and a_side_use:
        values = True
    elif a_angle_use and b_side_use:
        values = True
    elif a_angle_use and c_side_use:
        values = True
    elif b_angle_use and a_side_use:
        values = True
    elif b_angle_use and b_side_use:
        values = True
    elif b_angle_use and c_side_use:
        values = True
    elif a_side_use and b_side_use:
        values = True
    elif a_side_use and c_side_use:
        values = True
    elif b_side_use and c_side_use:
        values = True
    if not values:
        error_values = Label(text="""There are not enough values input,
please make sure at least one side is input
and at least two values are input""")
        error_values.grid(column=2, row=6)
    if values:
        calculate_values(a_side_use, b_side_use, c_side_use, a_angle_use, b_angle_use, a_side, b_side, c_side, a_rad,
                         b_rad)


def calculate_values(side_a_use, side_b_use, side_c_use, angle_a_use, angle_b_use, side_a, side_b, side_c, rad_a, rad_b):
    #########
    # sides #
    #########

    # for side a
    if not side_a_use:
        # decide on soh cah toa pythagoras
        # for soh
        if side_c_use and angle_a_use:
            # hypotenuse multiplied by sine of the angle
            side_a = side_c * math.sin(rad_a)
        # for cah
        elif side_c_use and angle_b_use:
            # hypotenuse multiplied by cosine of the angle
            side_a = side_c * math.cos(rad_b)
        # for toa
        elif angle_a_use and side_b_use:
            # adjacent multiplied by tangent of the angle
            side_a = side_b * math.tan(rad_a)
        elif angle_b_use and side_b_use:
            # opposite divided by tangent of the angle
            side_a = side_b / math.tan(rad_b)
        # for pythagoras
        elif side_b_use and side_c_use:
            # square root of hypotenuse squared minus other side squared
            side_a = math.sqrt((side_c ** 2) - (side_b ** 2))

    # for side b
    if not side_b_use:
        # decide on soh cah toa pythagoras
        # for soh
        if angle_b_use and side_b_use:
            # hypotenuse multiplied by sine of the angle
            side_b = side_c * math.sin(rad_b)
        # for cah
        elif angle_a_use and side_c_use:
            # hypotenuse multiplied by cosine of the angle
            side_b = side_c * math.cos(rad_a)
        # for toa
        elif angle_a_use and side_a_use:
            # opposite divided by tangent of the angle
            side_b = side_a / math.tan(rad_a)
        elif angle_b_use and side_a_use:
            # adjacent multiplied by tangent of the angle
            side_b = side_a * math.tan(rad_b)
        # for pythagoras
        elif side_a_use and side_c_use:
            # square root of hypotenuse squared minus other side squared
            side_b = math.sqrt((side_c ** 2) - (side_a ** 2))

    # for side c
    if not side_c_use:
        # decide on soh cah pythagoras
        # for soh
        if angle_a_use and side_a_use:
            # opposite divided by sine of the angle
            side_c = side_a / math.sin(rad_a)
        elif angle_b_use and side_b_use:
            # opposite divided by sine of the angle
            side_c = side_b / math.sin(rad_b)
        # for cah
        elif angle_a_use and side_b_use:
            # adjacent divided by cosine of the angle
            side_c = side_b / math.cos(rad_a)
        elif angle_b_use and side_a_use:
            # adjacent divided by cosine of angle
            side_c = side_a / math.cos(rad_b)
        # for pythagoras
        elif side_a_use and side_b_use:
            # square root of side a squared plus side b squared
            side_c = math.sqrt((side_a ** 2) + (side_b ** 2))

        # all sides have been calculated so they can be used in calculations
        side_a_use = True
        side_b_use = True
        side_c_use = True

    ##########
    # angles #
    ##########
    # if side a and the hypotenuse are used
    if side_a_use and side_c_use:
        # if the opposite angle is unknown
        if not angle_a_use:
            # use arc sine to determine the value
            rad_a = math.asin(side_a / side_c)
        # if the adjacent angle is unknown
        if not angle_b_use:
            # use arc cosine to determine the value
            rad_b = math.acos(side_a / side_c)
    # if side b and the hypotenuse are used
    if side_b_use and side_c_use:
        # if the adjacent angle is unknown
        if not angle_a_use:
            # use arc cosine to determine the value
            rad_a = math.acos(side_b / side_c)
        # if the opposite angle is unknown
        if not angle_b_use:
            # use arc sine to determine the value
            rad_b = math.asin(side_b / side_c)
    # if side a and side b are used
    if side_a_use and side_b_use:
        # if angle a is unknown
        if not angle_a_use:
            # angle a is arc tangent of the opposite side divided by the adjacent side
            rad_a = math.atan(side_a / side_b)
        # if angle b is unknown
        if not angle_b_use:
            # angle b is arc tangent of the opposite side divided by the adjacent side
            rad_b = math.atan(side_b / side_a)
    ############################
    # display the final values #
    ############################
    # make labels of the values
    final_angle_a = Label(text=("Radians:", round(rad_a, 2), "Degrees:", round(math.degrees(rad_a), 2)))
    final_angle_b = Label(text=("Radians:", round(rad_b, 2), "Degrees:", round(math.degrees(rad_b), 2)))
    final_side_a = Label(text=(round(side_a, 2), "units long"))
    final_side_b = Label(text=(round(side_b, 2), "units long"))
    final_side_c = Label(text=(round(side_c, 2), "units long"))

    # place values on GUI
    final_angle_a.grid(column=3, row=1)
    final_angle_b.grid(column=3, row=2)
    final_side_a.grid(column=3, row=3)
    final_side_b.grid(column=3, row=4)
    final_side_c.grid(column=3, row=5)


###########################
# setup misc gui elements #
###########################
# this helps the radio buttons not be both selected
a_variable = IntVar()
# radio button for selecting degrees
a_angle_degrees = Radiobutton(window, text="Degrees", value=1, command=degrees, variable=a_variable)
# radio button for selecting radians
a_angle_radians = Radiobutton(window, text="Radians", value=2, command=radians, variable=a_variable)

# button to press when all variables are input
done_button = Button(window, text="can not Input value", state="disabled", command=get_values)

###############################
# input value for angle A GUI #
###############################

# labels when angle A is input
a_angle_label = Label(text="angle A")
# angle A input box
a_angle_input = Entry(window, width=10)

# place the angle A label on the grid
a_angle_label.grid(column=0, row=1, padx=5)
# place the angle A input box on the grid
a_angle_input.grid(column=1, row=1, padx=5)

###############################
# input value for angle B gui #
###############################

# labels when angle B is input
b_angle_label = Label(text="angle B")
# angle B input box
b_angle_input = Entry(window, width=10)

# place the angle B label on the grid
b_angle_label.grid(column=0, row=2, padx=5)
# place the angle B input box on the grid
b_angle_input.grid(column=1, row=2, padx=5)

###############################
# input value for side a gui #
###############################

# labels when side a is input
a_side_label = Label(text="side a")
# side a input box
a_side_input = Entry(window, width=10)

# place the side a label on the grid
a_side_label.grid(column=0, row=3, padx=5)
# place the side a input box on the grid
a_side_input.grid(column=1, row=3, padx=5)

###############################
# input value for side b gui #
###############################

# labels when side b is input
b_side_label = Label(text="side b")
# side b input box
b_side_input = Entry(window, width=10)

# place the side b label on the grid
b_side_label.grid(column=0, row=4, padx=5)
# place the side b input box on the grid
b_side_input.grid(column=1, row=4, padx=5)

###############################
# input value for side c gui #
###############################

# labels when side c is input
c_side_label = Label(text="side c")
# side c input box
c_side_input = Entry(window, width=10)

# place the side c label on the grid
c_side_label.grid(column=0, row=5, padx=5)
# place the side c input box on the grid
c_side_input.grid(column=1, row=5, padx=5)

####################################
# place everything else on the GUI #
####################################
# place the radio buttons on the grid
a_angle_degrees.grid(column=1, row=0)
a_angle_radians.grid(column=2, row=0)
# place the done button on the grid
done_button.grid(column=3, row=6, padx=10)

# keep window running
window.mainloop()
