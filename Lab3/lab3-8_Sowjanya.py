# program - lab3-8_sowjanya.py  4 April 2019

'''
This program will perform the following actions:
1. ask for the input of number of people attending and number of hot dogs given to each person.
2. Calculates total number of hot dogs and buns required for the cookout.
3. display the minimum number of hot dogs and buns required and left over.

'''


# ========== Variable declarations.

people_count = 0
hotdog_count = 0
hotdog_pkg = 10     # number of hot dogs in a package
hotdog_buns_pkg = 8 # number of hot dog buns in a package
tot_hotdog = 0      # total hot dogs required
tot_buns = 0        # total hot dog buns required
req_hotdog = 0
req_buns = 0
extra_hotdogs = 0
extra_buns = 0
leftover_hotdogs = 0
leftover_buns = 0

# ========== Get the number of people attending the cookout.

people_count = int(input("Enter the total number of people attending the cookout: "))

# ========== Get the number of hot dogs per person.

hotdog_count = int(input("Enter the number of hot dogs each person will be given: "))

# ========== Calculate the total number of hot dogs, buns required.

tot_hotdog = people_count * hotdog_count
tot_buns = tot_hotdog

# ========== Calculate the total hot dog packages needed.

req_hotdog = tot_hotdog // hotdog_pkg

extra_hotdogs = tot_hotdog % hotdog_pkg

if extra_hotdogs > 0:
    req_hotdog = req_hotdog + 1
    leftover_hotdogs = hotdog_pkg - extra_hotdogs # Calculate left over hot dogs

# ========== Calculate the total hot dog buns packages needed.

req_buns = tot_buns // hotdog_buns_pkg

extra_buns = tot_buns % hotdog_buns_pkg 

if extra_buns > 0:
    req_buns = req_buns + 1;
    leftover_buns = hotdog_buns_pkg - extra_buns # Calculate left over buns
    

# ========== Display the results

print('The minimum number of pakcages of hot dogs required: ', req_hotdog)
print('The minimum number of pakcages of hot dog buns required: ', req_buns)
print('The number of hot dogs that will be left over: ', leftover_hotdogs)
print('The number of hot dog buns that will be left over: ', leftover_buns)

input('\n\npress enter to continue ')