from Q3_build_commands import build_line_commands

def draw_commands(t, commands, step_length):
    """
    Execute a list of commands using turtle.
    - step_length: độ dài cho mỗi 'F'
    """
    for cmd in commands:
        if cmd == "F":
            t.forward(step_length)
        elif cmd == "R60":
            t.right(60)
        elif cmd == "L60":
            t.left(60)
        elif cmd == "R120":
            t.right(120)
        elif cmd == "L120":
            t.left(120)


def polygon(t, sides, side_length, depth):
    """
    Draw a regular polygon using the command-based fractal line.
    """
    turn_angle = 360.0 / sides

    # 1) tạo commands cho 1 cạnh ở depth đó
    commands = build_line_commands(depth)

    # 2) tính độ dài bước cho mỗi 'F'
    # Vì mỗi lần depth tăng, cạnh bị chia 3 -> mỗi F nhỏ đi /3
    step_length = side_length / (3 ** depth)

    # 3) vẽ đủ sides cạnh
    for _ in range(sides):
        draw_commands(t, commands, step_length)
        t.right(turn_angle)