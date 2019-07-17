# program - lab7-13_sowjanya.py  26 April 2019

'''
This program simulates a Magic 8 Ball game, which is a fortune-telling toy
that displays a random response to a yes or no question. It performs the 
following actions:
1) Reads the 12 responses from the file named 8_ball_responses.txt
2) Prompts the user to ask a question
3) Displays random answers from the list using randint method
'''

import random # Needed for the randint method

def main():
    
    # Open file for reading
    infile = open('8_ball_responses.txt','r')
    
    #Read the contents of the file into a list.
    answerslist = infile.readlines()
    
    #close the file
    infile.close()

    play = 'y'
     
    while play == 'y':
        
        question = input('Please ask me a question:\n')
        
        # Generate random number between 0 and 10 as file has 11 answers
        number = random.randint(0,10)
        
        #Display the random answer
        print(answerslist[number])
        
        play = input('Do you want to play again? y = yes, anything else = no\n')
        print()
        

main()

input('\n\npress enter to continue ')