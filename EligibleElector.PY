# Author: Tega Omarejedje
# Assignment: Eligible Elector
# Date: 05/24/2025

# Step 1: Ask the User’s Age

# age takes the typed in integer age value from the user
age = int(input("How old are you? "))

# Step 2 & 4: Decide the Eligibility and Polish It Up

# checks if the user age is greater or equals to 18 before printing out the message.
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
# checks if the user age is less than 18, then does a calculation to find the age gap still needed to vote before printing out the message.
elif age < 18:
    # gap holds the user age difference from the required 18 to vote
    gap =  18 - age
    print("Oops! You’re not eligible yet. But hey, only %d more years to go!" %(gap)
)
    
