# program - lab4-16_sowjanya1.py  12 April 2019

'''
This program will perform the following actions:
1. ask for the input of number of squares to draw
2. Based on the input, draws a design using repaeated squares.
'''

# ==============================import the turtle graphics system
import turtle


# =========== Named constants

STARTING_LENGTH = 10
OFFSET = 5

# ========== Variable declarations.

num_squraes = 0
length = STARTING_LENGTH      # length of first square


# ============ask the user for input

num_squares = int(input('How many squares? '))

# =============Make sure it is not less than or equal to zero.
while num_squares <= 0:
    print('ERROR: Please enter a value greater than 0')
    num_squares = int(input('How many squares? '))
   
  

# =======Draw the squares

for count in range(num_squares):
    
    # =============hide the turtle
    turtle.hideturtle()
    
    # Draw the square
    
    for x in range(4):
        turtle.forward(length)
        turtle.left(90)
        
    length = length + OFFSET # increase the length of next square
        

# ============Keep the window open.
turtle.done()