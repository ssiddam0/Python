# Program lab7-4_Sowjanya.py 29 April 2019

'''
This program generates a list of random numbers and uses bubble sort technique
to sort the numbers. And displays the lowest number, highest number, total and 
average of the sorted list

'''
 
import random # Needed for the randint method

def main():
    
    list_len = int(input('How many numbers you want to generate in the range of 1-100?\n'))
    
    # Create a list to hold the random numbers
    numbers = [0] * list_len 
    
    index = 0
    total = 0  # Total of the list elements
    
    #Generate the random numbers and calculate the total of the list
    while index < len(numbers):
        numbers[index] = random.randint(1,100)
        total += numbers[index]
        index += 1
        
    # Calculate the average of the elements.
    average = total / len(numbers)
        
    print('Here is the list generated before sorting: ', numbers)
    
    # Bubble sort technique to sort the numbers
    for i in range(list_len-1, 0, -1):
        for j in range(0, i, 1):
            if numbers[j] > numbers[j+1]: # Swap technique using temporary variable
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
                
    
    # Display the results
    print('Here is the list after sorting: ', numbers)
    print('The lowest number in the list: ', numbers[0])
    print('The highest number in the list: ', numbers[list_len-1])
    print('The total of the numbers in the list: ', total)
    print('The average of the numbers in the list: ', format(average,'0.2f'))
    

# call the main method
main()

input('\n\npress enter to continue ')