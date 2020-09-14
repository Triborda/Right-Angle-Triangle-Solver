#########################
# import needed modules #
#########################
from tkinter import *
import math

####################
# preset variables #
####################
# used in a function to stop overlap of labels
done = False

# SOH CAH TOA deciding variables
a_angle_use = False
b_angle_use = False
a_side_use = False
b_side_use = False
c_side_use = False

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
    # get needed variables from the global
    global angle_type, a_angle_input, done
    if a_angle_input.get() != "" and isinstance(a_angle_input.get(), str):
        # if the angles are in degrees
        if angle_type == "deg":
            # get the value and convert to integer then radians
            a_angle_rad = math.radians(float(a_angle_input.get()))
            # get the value and convert to integer
            a_angle_deg = float(a_angle_input.get())
        # else if the angle type is in radians
        elif angle_type == "rad":
            # set the angle to the value in radians
            a_angle_rad = float(a_angle_input.get())
            # set the angle to the value in degrees
            a_angle_deg = math.degrees(float(a_angle_input.get()))
        print("angle A has {} Degrees or {} radians".format(a_angle_deg, a_angle_rad))
        # variable to make deciding on SOH CAH TOA easier
        a_angle_use = True
    else:
        print("angle A is unknown")

    if b_angle_input.get() != "" and isinstance(b_angle_input.get(), str):
        # if the angles are in degrees
        if angle_type == "deg":
            # get the value and convert to integer then radians
            b_angle_rad = math.radians(float(b_angle_input.get()))
            # get the value and convert to integer
            b_angle_deg = float(b_angle_input.get())
        # else if the angle type is in radians
        elif angle_type == "rad":
            # set the angle to the value in radians
            b_angle_rad = float(b_angle_input.get())
            # set the angle to the value in degrees
            b_angle_deg = math.degrees(float(b_angle_input.get()))
        print("angle B has {} Degrees or {} radians".format(b_angle_deg, b_angle_rad))
        # variable to make deciding on SOH CAH TOA easier
        b_angle_use = True
    else:
        print("angle B is unknown")

    if a_side_input.get() != "" and isinstance(a_side_input.get(), str):
        print("side a is {} units long".format(a_side_input.get()))
        # variable to make deciding on SOH CAH TOA easier
        a_side_use = True
    else:
        print("side a is unknown")

    if b_side_input.get() != "" and isinstance(b_side_input.get(), str):
        print("side b is {} units long".format(b_side_input.get()))
        # variable to make deciding on SOH CAH TOA easier
        b_side_use = True
    else:
        print("side b is unknown")

    if c_side_input.get() != "" and isinstance(c_side_input.get(), str):
        print("side c is {} units long".format(c_side_input.get()))
        # variable to make deciding on SOH CAH TOA easier
        c_side_use = True
    else:
        print("side c is unknown")

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
