# program - lab3-16_sowjanya.py  4 April 2019

'''
This program determines whether the year entered is a leap year or not
and displays the number of days in February that year.

'''


# ========== Variable declarations.

year = 0

# ========== Get the year.

year = int(input("Enter a year: "))

# ========== Determine if the year is a leap year or not.

if (year % 100) == 0: 
    if (year % 400) == 0:   # checks whether year is evenly divisible by 100 and 400
        print('In',year, 'February has 29 days.')
    else:
        print('In',year, 'February has 28 days.')
        
elif (year % 4) == 0:       # if not divisible by 100, checks if divisible by 4
    print('In',year, 'February has 29 days.')
else:
    print('In',year, 'February has 28 days.')
    
input('\n\npress enter to continue ')