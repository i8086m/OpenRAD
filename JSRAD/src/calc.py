
# RideLogic Bike Calculator port
# Early Python implementation

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
    
    

class Bike:
    def __init__(self,
                head_angle,
                reach,
                stack,
                setback,
                rise,
                stem_length,
                stem_angle,
                half_stack):
        self.head_angle = head_angle
        self.reach = reach
        self.stack = stack
        self.setback = setback
        self.rise = rise
        self.stem_length = stem_length
        self.stem_angle = stem_angle
        self.half_stack = half_stack
        
        


    def get_rad(self):
        inverse_stem_angle = 90 - self.stem_angle
        inverse_head_angle = 90 - self.head_angle
        inverse_total_angle = inverse_head_angle + self.stem_angle


        head_angle_sin = sin(inverse_head_angle * pi / 180)
        head_angle_cos = cos(inverse_head_angle * pi / 180)

        total_angle_sin = sin(inverse_total_angle * pi / 180)
        total_angle_cos = cos(inverse_total_angle * pi / 180)


        stem_frame_offset = -head_angle_sin * self.half_stack
        stem_angle_offset = total_angle_cos * self.stem_length


        effective_bar_height_small_triangle = head_angle_cos * self.half_stack
        effective_bar_height_big_triangle = total_angle_sin * self.stem_length
        
        effective_bar_height = effective_bar_height_small_triangle + effective_bar_height_big_triangle + self.rise
       
        effective_bar_length = stem_frame_offset + stem_angle_offset - self.setback

        effective_reach = effective_bar_length + self.reach
        effective_stack = effective_bar_height + self.stack

        total_rad = sqrt(effective_reach**2 + effective_stack**2)

        total_rad_angle = atan2(effective_stack, effective_reach) * (180 / pi)


        print('Effective Reach:', effective_reach)
        print('Effective Reach:', effective_stack)
        print('RAD:', total_rad)
        print('RAD Angle:', total_rad_angle)
        
        return (total_rad, total_rad_angle)



    def get_sho(self):
        stem_level_angle = radians(90 - self.head_angle + self.stem_angle)
        stem_vertical_angle = radians(self.head_angle - self.stem_angle)

        full_angle = stem_level_angle + stem_vertical_angle

        effective_stem_height = self.stem_length * sin(stem_level_angle)
        effective_stem_length = self.stem_length * sin(stem_vertical_angle)

        bar_height = effective_stem_height + self.rise
        bar_distance = effective_stem_length - self.setback

        second = tan(radians(90 - self.head_angle)) * bar_height
        
        return second + bar_distance


bike = Bike(
    head_angle = 65,
    reach = 445,
    stack = 652,
    setback = 50,
    rise = 20,
    stem_length = 35,
    stem_angle = 0,
    half_stack = 30,
)


print(bike.get_rad())
print(bike.get_sho())