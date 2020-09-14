##################
# import modules #
##################

import math

#####################
# find unknown side #
#####################


# for side a
if not a_side_use:
    # decide on soh cah toa pythagoras
    # for soh
    if c_side_use and a_angle_use:
        # hypotenuse multiplied by sine of the angle
        a_side = c_side * math.sin(a_angle_rad)
    # for cah
    elif c_side_use and b_angle_use:
        # hypotenuse multiplied by cosine of the angle
        a_side = c_side * math.cos(b_angle_rad)
    # for toa
    elif a_angle_use and b_side_use:
        # adjacent multiplied by tangent of the angle
        a_side = b_side * math.tan(a_angle_rad)
    elif b_angle_use and b_side_use:
        # opposite divided by tangent of the angle
        a_side = b_side / math.tan(b_angle_rad)
    # for pythagoras
    elif b_side_use and c_side_use:
        # square root of hypotenuse squared minus other side squared
        a_side = math.sqrt((c_side ** 2) - (b_side ** 2))
    # display the final value
    print("side a is", a_side, "units long")

# for side b
if not b_side_use:
    # decide on soh cah toa pythagoras
    # for soh
    if b_angle_use and c_side_use:
        # hypotenuse multiplied by sine of the angle
        b_side = c_side * math.sin(b_angle_rad)
    # for cah
    elif a_angle_use and c_side_use:
        # hypotenuse multiplied by cosine of the angle
        b_side = c_side * math.cos(a_angle_rad)
    # for toa
    elif a_angle_use and a_side_use:
        # opposite divided by tangent of the angle
        b_side = a_side / math.tan(a_angle_rad)
    elif b_angle_use and a_side_use:
        # adjacent multiplied by tangent of the angle
        b_side = a_side * math.tan(b_angle_rad)
    # for pythagoras
    elif a_side_use and c_side_use:
        # square root of hypotenuse squared minus other side squared
        b_side = math.sqrt((c_side ** 2) - (a_side ** 2))
    # display the final value
    print("side b is", b_side, "units long")

# for side c
if not c_side_use:
    # decide on soh cah pythagoras
    # for soh
    if a_angle_use and a_side_use:
        # opposite divided by sine of the angle
        c_side = a_side / math.sin(a_angle_rad)
    elif b_angle_use and b_side_use:
        # opposite divided by sine of the angle
        c_side = b_side / math.sin(b_angle_rad)
    # for cah
    elif a_angle_use and b_side_use:
        # adjacent divided by cosine of the angle
        c_side = b_side / math.cos(a_angle_rad)
    elif b_angle_use and a_side_use:
        # adjacent divided by cosine of angle
        c_side = a_side / math.cos(b_angle_rad)
    # for pythagoras
    elif a_side_use and b_side_use:
        # square root of side a squared plus side b squared
        side_c = math.sqrt((a_side ** 2) + (b_side ** 2))
    # display the final value
    print("side c is", c_side, "units long")
