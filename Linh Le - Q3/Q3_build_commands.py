# Step1: Build drawing commands using recursion
# Commands:
#   'F'  : move forward
#   'L60': turn left 60 degrees
#   'R60': turn right 60 degrees
#   'L120', 'R120' similarly

def build_line_commands(depth):
    """
    Return a list of commands to draw the fractal line at given depth.
    Depth 0: ['F']
    Depth > 0: F, R60, F, L120, F, R60, F   (mỗi F là 1 đoạn nhỏ)
    """
    if depth == 0:
        return ["F"]

    prev = build_line_commands(depth - 1)

    # Quy tắc: line -> line R60 line L120 line R60 line
    return prev + ["R60"] + prev + ["L120"] + prev + ["R60"] + prev