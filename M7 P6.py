#Greg Brewer
# 5/28/2023
# Problem 6 draw polygon

def draw_polygon(num_sides, side_length):
    angle = 360 / num_sides
    for _ in range(num_sides):
        forward(side_length)
        right(angle)

# Call the function to create the pattern
for i in range(3, 9):
    draw_polygon(i, 50)



