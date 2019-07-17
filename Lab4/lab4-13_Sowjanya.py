# program - lab4-13_sowjanya.py  12 April 2019

'''
This program predicts the approximate size of a population of organixms.
It will perform the following actions:
1. ask for the input of starting number of organisms, percentage of 
   population increase, number of days to multiply.
2. Uses loops to iterate over the data to calculate total population
3. display the day and corresponding population

'''
# ==========================================Variable declarations

startingNumOfOrganisms = 0
dailyIncrease = 0.0
daysLeft = 0
approxPopulation = 0.0

# =======================================Get the data.

startingNumOfOrganisms = int(input("Enter the starting number of organisms: "))

dailyIncrease = float(input('Enter the daily increase as a percentage: '))

daysLeft = int(input('Enter the number of days to multiply: '))

approxPopulation = startingNumOfOrganisms

# =============calculate the daily increase percentage(ex: 20% = 0.2)
dailyIncrease = dailyIncrease / 100

# ========Program keeps running until user enters 0 as starting number of organisms

while startingNumOfOrganisms!= 0 :
    print()
    print('#Day', '\t', 'Population')
    for count in range(1, daysLeft+1):
        print(count, '\t', approxPopulation)
        approxPopulation += (approxPopulation * dailyIncrease)
        
    startingNumOfOrganisms = int(input("\nEnter the new starting number of organisms or 0 to stop: "))
    approxPopulation = startingNumOfOrganisms

