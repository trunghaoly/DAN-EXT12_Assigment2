# Step 1: Draw a line
def line(t, length, depth, inward = True):
   
    if depth == 0:
        t.forward(length)
        return

    L = length / 3.0

    line(t, L, depth - 1)
    t.right(60)
    line(t, L, depth - 1)
    t.left(120)
    line(t, L, depth - 1)
    t.right(60)
    line(t, L, depth - 1)