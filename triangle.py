import simple_draw as sd

length = 200
point_0 = sd.get_point(300, 300)

def triangle(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw()

for angle in range(1000, 3680, 15):
    triangle(point=point_0, angle=angle)

sd.pause()
