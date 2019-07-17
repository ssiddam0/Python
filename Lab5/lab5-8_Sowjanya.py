# program - lab5-8_sowjanya.py  19 April 2019

'''
This program uses the modular design approach to calculate the total cost of the paint job 
and labor charges given the square feet of wall space to be painted.
1) main() method is used to get the data from the user and call the remaining functions 
2) calculate_cost() method is used to calculate the estimated charges
3) print_Results() method is used to print the data.

'''


# ==Constants, For every 250 sqft of wall space, 8 hours of labor and $35 per hour

SQFT_GAL = 250
LABOR_HRS = 8
LABOR_CHARGE_HR = 35

# ======= main() method is used to get the user input and call the other methods

def main():
    
    # =======================================Get the data.
    
    space_sqrft = int(input("Enter the space to be painted in square feet: "))
    
    paint_price = float(input('Enter the price of the paint per gallon: '))
    
    calculate_cost(space_sqrft, paint_price)  #  call the calculate_cost method
    return

def calculate_cost(sqrft, paint_price):
    tot_paint_gal = sqrft / SQFT_GAL               # Number of gallons of paint required
    
    tot_paint_cost = tot_paint_gal * paint_price   # Total cost of the paint
    
    tot_lab_hrs = (LABOR_HRS * sqrft) / SQFT_GAL   # Total hours of labor required
    
    tot_lab_cost = tot_lab_hrs * LABOR_CHARGE_HR   # Total labor charges
    
    tot_cost = tot_lab_cost + tot_paint_cost       # Total cost of the paint job
    
    printResults(tot_paint_gal, tot_lab_hrs, tot_paint_cost, tot_lab_cost, tot_cost)  # call the printResults method
    
    return

def printResults(tot_paint_gal, tot_lab_hrs, tot_paint_cost, tot_lab_cost, tot_cost):
    
    print('The number of gallons of paint required: ',tot_paint_gal)
    print('The hours of labor required: ',format(tot_lab_hrs,'.0f'))
    print('The cost of the paint: $',format(tot_paint_cost,'.2f'))
    print('The labor charges: $',format(tot_lab_cost,'.2f'))
    print('The total cost of the paint job: $',format(tot_cost,'.2f'))
    
    return
    
    
main()  # calling main method

input('\n\npress enter to continue ')