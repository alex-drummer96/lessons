import simple_draw as sd
sd.resolution = (1200, 600)

point = sd.get_point(300, 5)

#
# def branch(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
#     v1.draw()
#     return v1.end_point
#
# angle_0 = 90
# length_0 = 200
# next_point = branch(point=point, angle=angle_0, length=length_0)
# next_angle = angle_0-30
# next_length = length_0 * 0.75
# next_point = branch(point=next_point, angle=next_angle, length=next_length)
# next_angle = next_angle-30
# next_length = next_length * 0.75
# next_point = branch(point=next_point, angle=next_angle, length=next_length)
# next_point = point
# next_angle = angle_0
# next_length = length_0
# while next_length > 1:
#     next_point = branch(point=next_point, angle=next_angle, length=next_length)
#     next_angle = next_angle-30
#     next_length = next_length * 0.75

def branch(point, angle, length, delta):
    if length < 1:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle-delta
    next_length = length * 0.75
    branch(point=next_point, angle=next_angle, length=next_length, delta=delta)

for delta in range(-50, 1, 10):
    branch(point=point, angle=90, length=100, delta=delta)
for delta in range(0, 51, 10):
    branch(point=point, angle=90, length=100, delta=delta)
sd.pause()
