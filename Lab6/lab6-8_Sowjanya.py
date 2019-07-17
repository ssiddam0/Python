
# program - lab6-8_sowjanya.py  25 April 2019

'''
This program reads the random numbers from randomNumber.txt file. Displays 
the total of the numbers and the number of random numbers read from the file.

'''
def main():
    
    # Open the randomNumber.txt file in read mode
    random_file = open('randomNumber.txt','r')
    
    total = 0  # used to hold total of the numbers
    count = 0  # used to hold number of random numbers
    
    #iterate through each line in the file
    for line in random_file:
        
        #Convert string to int
        number = int(line)
        total += number
        count += 1
        
    # Close the file
    random_file.close()
    
    # Display the results
    print('The total of the numbers: ',total)
    print('The number of random numbers read from the file: ',count)
    
#Call the main function
main()

input('\n\npress enter to continue ')