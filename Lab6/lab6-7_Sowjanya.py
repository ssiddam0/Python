
# program - lab6-7_sowjanya.py  25 April 2019

'''
This program gets the number of random numbers from the user and saves it as 
records in the randomNumber.txt file.

'''
import random  # Needed for the randrange function
def main():
    
    # Get the number of random numbers to write into the file
    num_count = int(input('How many random numbers the file should hold?: '))
    
    # Open the file for writing
    random_file = open('randomNumber.txt','w')
    
    
    for count in range(num_count):
        
        #Get the random number in the range of 1 through 500
        number = random.randrange(1,501)
        
        # write the data as record to the file
        random_file.write(str(number)+'\n')
        
    #close the file
    random_file.close()
    print('Random numbers are written to randomNumber.txt.')
        
#Call the main function
main()

input('\n\npress enter to continue ')        
        
    