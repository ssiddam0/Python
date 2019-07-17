# program - lab5-23_sowjanya.py  19 April 2019

'''
This program is used to draw the snow man using turtle graphics system.
This program uses modular design with functions to draw various parts of the snow man
such as body, head, hat, scarf, 
'''


import turtle  # ========= import turtle graphics system


# ======= main() function calls all other functions

def main():
    
    turtle.hideturtle()
    
    drawBase()             # Draw base of the snowman 
    
    drawMidSection()       # Draw the middle snowball

    drawHead()             # Draw the snowman's head, with eyes and smile/mouth
    
    drawArms()             # Draw snowman's arms
    
    drawHat()              # Draw snowman's hat   
    
    drawScarf()            # Draw snowman's scarf
    
    
    return

# ===== This function is used to draw circle with radius passed, starting  at (x,y) cordinates

def circle(x,y,radius):
    turtle.penup()        # Raise the pen
    turtle.goto(x,y)      # Position the turtle
    turtle.pendown()      # Lower the pen
    turtle.circle(radius) # Draw a circle
    
    return

# ===== This function is used to draw line from (startx,starty) to (endx,endy)
def line(startx, starty, endx, endy):
    turtle.penup()
    turtle.goto(startx, starty)   # Move to the starting point
    turtle.pendown()
    turtle.goto(endx, endy)       # Draw a line to the ending point
    
    return

def drawBase():
    circle(0, -150, 75)  # draw a circle with 75 radius at (0,-150) position
    
    return

def drawMidSection():
    circle(0,0,50)  # draw a circle with 50 radius at (0,0) position
    
    return

def drawHead():
    circle(0,100,30)  # draw a circle with 30 radius at (0,100) position
    
    circle(10,140,3)  # draw right eye
    
    circle(-10,140,3) # draw left eye
    
    turtle.penup()
    turtle.goto(-15,130)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.circle(15,180)    # draw smile/mouth
    
    return

def drawArms():
    line(-50,50,-80,60)      # call the line() method with specified coordinates.
    line(-80,60,-90,90)
    line(-90,90,-100,95)
    line(-90,90,-90,100)
    line(50,50,90,80)
    line(90,80,90,90)
    line(90,80,100,78)
    
    return

def drawHat():
    turtle.pensize(8)     # increase thickness of line 
    line(-40,155,40,155) 
    turtle.penup()
    turtle.goto(-15,155)
    turtle.pendown()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.setheading(0)
    for x in range(4):       # Draw square part of the hat
        turtle.forward(30)
        turtle.left(90)      
    turtle.end_fill()  
    
    return

def drawScarf():
    turtle.penup()
    turtle.goto(-15,100)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.pencolor('red')
    turtle.circle(15,180)    
    turtle.penup()
    turtle.goto(0,85)
    turtle.pendown()
    line(0,85,-15,70)
    turtle.penup()
    turtle.goto(0,85)
    turtle.pendown()
    line(0,85,15,70)
    
    return 

# ============Call the main() method
main()

# ============Keep the window open.
turtle.done()
    