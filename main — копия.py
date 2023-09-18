'''
RideLogic™ Bike Calculator
Simplified March 19, 2023.

Guesswork, anxiety and wasted money end here. Buy the perfect frame, stem and handlebars for your body and riding style. Do the math before you spend $,$$$!

Step 1: Measure your body RAD
For directions, check out this lesson on measuring your RAD with a RipRow or broomstick

if you don’t want to measure, or as a check of your measurement, you should calculate your body RAD.

Step 2: Calculate the dimensions of your new setup
In the fields below, measurements for the frame, stem and handlebar you’re thinking about buying. Tweak those parameters until you get the RAD, RAD Angle and SHO you want. In order of importance:

RAD. Rider Area Distance. Distance from bottom bracket to midpoint of the grips. This is the most important number. Your bike RAD should match your body RAD.
RAD Angle. Formerly known as RAAD. Angle of RAD compared with level. This is second most important. Most riders are best with a RAD Angle between 58 and 60 degrees.
SHO. Steering/hands offset. Horizontal distance between the center of the stem clamp area and the midpoint of the grips .The closer to zero millimeters the better. But this is tertiary to RAD and RAD Angle.


Frame information
These numbers are listed in your frame's specs. If you've changed your shock length, fork length or tire size (if front is different from rear) it would be smart to re-measure.
Head angle (degrees)
65
This is the head angle of your frame.
Frame reach (mm)
445
This is the reach of your frame, aka the horizontal distance between the bottom bracket and head tube.
Frame rise or stack (mm)
652
This is the rise (or stack) of your frame, aka the vertical distance between the bottom bracket and head tube.
Stem and handlebar information
Accuracy is important. Look up the specs you can (handlebar rise, stem length, stem angle and head angle). Measure the rest (handlebar setback, half stack).
Handlebar setback (mm)
50
With bar at neutral angle, how far are the grips behind the center of the clamp area? Average riser bars are about 30mm. Learn about handlebar setback here.
Handlebar rise (mm)
25
This is printed on the handlebar or its packaging (eg 10mm). You can measure this while you measure setback
Stem length (mm)
45
This is almost always printed on the stem (eg 50mm). If not, measure from the middle of the steerer tube clamp area to the middle of the handlebar clamp.
Stem angle (degrees)
7
This is the amount of rise (eg 8°) or drop (eg -8°). This number is printed on the stem, it's packaging or online. If your stem has drop or is upside down, enter a negative number (eg -10).
Half stack (mm)
31
This is the distance from the middle of the top of the frame's head tube to the middle of the stem's steerer tube clamp area. This number includes the top of the head seat, spacers under the stem and half of the stem's clamp height. 25mm is pretty average. See this image.
New cockpit information
Based on the stem, handlebar and frame information you entered, here are the RAD, reach and stack of your bike's entire cockpit (from the bottom bracket to the handlebars.)
How does this compare with the numbers you generated with the RideLogic Cockpit Calculator?
When setting up your bike, make RAD as close to perfect as you can.
When your bike's RAD is a bit longer than your ideal, you sacrifice power and control (the last 10mm is magic).
When your bike's RAD is a bit shorter than your ideal, that can work very well. You see this with some downhillers and freestylers (and a lot of very tall people).

'''

from math import sin, cos, pi, sqrt, atan2, tan

def rot(v, angle):
    x = v[0] * cos(angle) - v[1] * sin(angle)
    y = v[0] * sin(angle) + v[1] * cos(angle)
    return [x, y]

def add(v1, v2):
    return [sum(x) for x in zip(v1, v2)]

def radians(f):
    return f * pi / 180
    
def degrees(f):
    return f * (180 / pi)


head_angle = 65
reach = 470
stack = 652

setback = 50
rise = 20
stem_length = 35
stem_angle = 0
half_stack = 30



inverse_stem_angle = 90 - stem_angle
inverse_head_angle = 90 - head_angle
inverse_total_angle = inverse_head_angle + stem_angle


handlebar_setback_negative = -setback

head_angle_sin = sin(inverse_head_angle * pi / 180)
head_angle_cos = cos(inverse_head_angle * pi / 180)

total_angle_sin = sin(inverse_total_angle * pi / 180)
total_angle_cos = cos(inverse_total_angle * pi / 180)


stem_frame_offset = -head_angle_sin * half_stack
stem_angle_offset = total_angle_cos * stem_length


effective_stem_bar_length = stem_frame_offset + stem_angle_offset + handlebar_setback_negative


effective_bar_stem_height_small_triangle = head_angle_cos * half_stack
effective_bar_stem_height_big_triangle = total_angle_sin * stem_length

effective_bar_stem_height = effective_bar_stem_height_small_triangle + effective_bar_stem_height_big_triangle + rise



effective_reach = effective_stem_bar_length + reach
effective_stack = effective_bar_stem_height + stack

total_rad = sqrt(effective_reach**2 + effective_stack**2)

total_rad_angle = atan2(effective_stack, effective_reach) * (180 / pi)


print('Effective Reach:', effective_reach)
print('Effective Reach:', effective_stack)
print('RAD:', total_rad)
print('RAD Angle:', total_rad_angle)


head_angle = 60
setback = 40
rise = 55
stem_length = 50
stem_angle = 15

stem_level_angle = radians(90 - head_angle + stem_angle)
stem_vertical_angle = radians(head_angle - stem_angle)

full_angle = stem_level_angle + stem_vertical_angle

effective_stem_height = stem_length * sin(stem_level_angle)
effective_stem_length = stem_length * sin(stem_vertical_angle)

print(effective_stem_height)
print(effective_stem_length)

bar_height = effective_stem_height + rise
bar_distance = effective_stem_length - setback

second = tan(radians(90 - head_angle)) * bar_height
print(bar_height)
print(second + bar_distance)