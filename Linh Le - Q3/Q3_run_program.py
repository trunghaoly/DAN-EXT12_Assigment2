import turtle
from Q3_draw_polygon import polygon

def read_user_inputs():
    while True:
        try:
            sides = int(input("Enter the number of sides (>=3): ").strip())
            side_length = float(input("Enter the side length (pixels, >0): ").strip())
            depth = int(input("Enter the recursion depth (>=0): ").strip())

            if sides < 3:
                print("Caution: The number of sides must >= 3.\n")
                continue
            if side_length <= 0:
                print("Caution: The side length must > 0.\n")
                continue
            if depth < 0:
                print("Caution: The recursion depth must >= 0.\n")
                continue

            return sides, side_length, depth

        except ValueError:
            print("Warning: Must enter a number.\n")

def main():
    sides, side_length, depth = read_user_inputs()

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(3)

    polygon(t, sides, side_length, depth)

    turtle.done()

if __name__ == "__main__":
    main()