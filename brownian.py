"""
==============================================================
brownian.py is a turtle walker with brownian motion to start.

A generation ends with the walker reaches a distance of 400.
Subsequent generations use a modification of the shortest path to 400.

When the walker reachs 400 in 10 or less moves the walker stops.
==============================================================
"""

### I should just load the portions of the packages I use.
import turtle
import random
import math

### just some shortcuts
random.seed()
rr: 'randomrange' = random.randrange
ri: 'randomint' = random.randint

### start the turtle
turtle.colormode(255)
turtle.bgcolor('black')
# turtle.setundobuffer(None) # this doens't appear to speed things up
turtle.title('Brownian Turtle Evolves')

t = turtle.Turtle()
t.speed(0)
t.width(2)

gen: 'Walker generation' = 0

t.penup()
t.goto(-460, 350)
t.setheading(0)
t.pendown()
t.color('white')
t.write(f"Gen: {gen}", font=('Courier New', 20, 'normal'))
t.penup()
t.goto(0, 0)
t.pendown()

## gen 0 is completely random
### initialize the pen color
r: 'red' = rr(256)
g: 'green' = rr(256)
b: 'blue' = rr(256)

best_moves = []
while (t.xcor() ** 2 + t.ycor() ** 2) < 160000:
    l: 'left turn' = rr(360)
    t.left(l)

    r += ri(-10, 10)
    if not (0 <= r <= 255):
        r = rr(256)
    b += ri(-10, 10)
    if not (0 <= b <= 255):
        b = rr(256)
    g += ri(-10, 10)
    if not (0 <= g <= 255):
        g = rr(256)
    t.color(r, b, g)
    f: 'forward' = ri(3, 10)
    t.forward(f)
    best_moves.append([r, b, g, l, f])

### gen 0 is current best.
### Use current best for next gen
best_gen = 0
best_dist = math.sqrt(t.xcor() ** 2 + t.ycor() ** 2)
best_len = len(best_moves)
old_best = best_gen
old_dist = best_dist
old_len = best_len

### loop as long as it takes for best to take more than 10 moves
while best_len > 10:
    ### modify the description
    ### hide old descripton
    t.setheading(0)
    t.penup()
    t.goto(-460, 370)
    t.pendown()
    t.color('black')
    t.write(f"Best: Gen{old_best} reached {old_dist:.2f} in {old_len} moves",
            font=('Courier New', 20, 'normal'))
    t.penup()
    t.goto(-460, 370)
    t.pendown()
    t.color('white')
    t.write(f"Best: Gen{best_gen} reached {best_dist:.2f} in {best_len} moves",
            font=('Courier New', 20, 'normal'))
    t.penup()
    t.goto(-460, 350)
    t.pendown()
    t.color('black')
    t.write(f"Gen: {gen}", font=('Courier New', 20, 'normal'))
    t.penup()
    t.goto(-460, 350)
    gen += 1  # now the generaton number can be increased
    t.pendown()
    t.color('white')
    t.write(f"Gen: {gen}", font=('Courier New', 20, 'normal'))

    ### move to start
    t.penup()
    t.goto(0, 0)
    t.pendown()
    new_moves = []

    l_add: 'additonal left when prior forward is 0' = 0
    for r, b, g, l, f in best_moves:

        r += ri(-5, 5)
        if not (0 <= r <= 255):
            r = rr(256)
        b += ri(-5, 5)
        if not (0 <= b <= 255):
            b = rr(256)
        g += ri(-5, 5)
        if not (0 <= g <= 255):
            g = rr(256)
        t.color(r, b, g)

        f += ri(-2, 2)
        if f == 0:
            # when forward == 0 just change the next move's left turn
            l_add = (l + l_add + 360 + ri(-1, 1)) % 360
        else:
            if f < 0:
                # when forward < 0 adjust the left turn and make f positive
                l_add += 180
                f = -f
            l = (l + l_add + 360 + ri(-1, 1)) % 360
            l_add = 0
            t.forward(f)
            t.left(l)
            new_moves.append([r, b, g, l, f])

        if (t.xcor() ** 2 + t.ycor() ** 2) >= 160000:

            ### is this a new best?
            if len(new_moves) < best_len:
                old_best = best_gen
                old_dist = best_dist
                old_len = best_len
                best_gen = gen
                best_moves = new_moves
                best_dist = math.sqrt((t.xcor() ** 2 + t.ycor() ** 2))
                best_len = len(best_moves)
                break
